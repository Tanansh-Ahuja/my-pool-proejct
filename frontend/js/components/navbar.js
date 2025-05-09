export async function loadNavbar() {
  const navbarPlaceholder = document.getElementById("navbar-placeholder");
  if (!navbarPlaceholder) return;

  try {
    const res = await fetch("/frontend/navbar.html");
    const html = await res.text();
    navbarPlaceholder.innerHTML = html;

    const navLinks = document.getElementById("nav-links");
    const hamburger = document.getElementById("hamburger");
    const token = localStorage.getItem("access_token");

    // Event listener for the hamburger icon
    hamburger.addEventListener("click", () => {
      const navRight = document.querySelector(".nav-right");
      navRight.classList.toggle("active");
    });

    if (!token) {
      navLinks.innerHTML = `
        <a href="/frontend/index.html">Home</a>
        <a href="/frontend/login.html">Login</a>
      `;
    } else {
      const headers = {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      };
      const userRes = await fetch("http://localhost:8000/customers/me", {
        headers,
      });

      if (!userRes.ok) throw new Error("Invalid token");

      const user = await userRes.json();

      if (user.role === "customer") {
        navLinks.innerHTML = `
          <a href="/frontend/index.html">Home</a>
          <a href="/frontend/pages/customer/booking_create.html">Book Now</a>
          <a href="/frontend/pages/customer/view_bookings.html">Bookings</a>
          <a href="/frontend/pages/customer/customer_profile.html">Profile</a>
          <a href="#" id="logout-link">Logout</a>
        `;

        document.getElementById("logout-link").addEventListener("click", () => {
          localStorage.removeItem("access_token");
          window.location.href = "/frontend/index.html";
        });
      } else {
        // Temporary fallback for admins
        navLinks.innerHTML = `
            <a href="/frontend/pages/admin/admin.html">Home</a>
            <a href="/frontend/pages/admin/view_bookings.html">View Bookings</a>
            <a href="/frontend/pages/admin/view_revenue.html">View Revenue</a>
            <a href="/frontend/pages/customer/customer_profile.html">Profile</a>
            <a href="#" id="logout-link">Logout</a>
          `;

          document.getElementById("logout-link").addEventListener("click", () => {
            localStorage.removeItem("access_token");
            window.location.href = "/frontend/index.html";
          });
          
      }
    }
  } catch (err) {
    console.error("Navbar loading failed:", err);
  }
}

loadNavbar();
