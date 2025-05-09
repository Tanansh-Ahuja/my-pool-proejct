document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("login-form");
    const passwordInput = document.getElementById("password");
    const toggleIcon = document.getElementById("toggle-password");
  
    // Toggle password visibility
    toggleIcon.addEventListener("click", () => {
      const isPassword = passwordInput.type === "password";
      passwordInput.type = isPassword ? "text" : "password";
      toggleIcon.textContent = isPassword ? "🙈" : "👁️";
    });
  
    // Handle login
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
  
      const uemail = form.email.value;
      const upassword = form.password.value;
  
      try {
        const response = await fetch("http://localhost:8000/auth/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email:uemail, password:upassword }),
        });
  
        const data = await response.json();
  
        if (response.ok && data.access_token) {
          console.log("inside if");
          localStorage.setItem("access_token", data.access_token);
          const headers = {
            Authorization: `Bearer ${data.access_token}`,
            "Content-Type": "application/json",
          };
          const userRes = await fetch("http://localhost:8000/customers/me", {
            headers,
          });
          console.log(userRes);
          if (!userRes.ok) throw new Error("Invalid token");
          const user = await userRes.json();
          if (user.role === "customer") {
            window.location.href = "./pages/customer/customer_bookings.html"; // redirect to next page
          } else {
            // Temporary fallback for admins
            window.location.href = "/frontend/pages/admin/admin.html"; // redirect to next page
          }
          
        } else {
          alert(data.detail || "Login failed.");
        }
      } catch (error) {
        console.error("Login error:", error);
        alert("An error occurred while logging in.");
      }
    });
  });
  

  