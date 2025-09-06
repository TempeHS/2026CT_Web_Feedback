const toastTrigger = document.getElementById("liveToastBtn");
const toastContainer = document.getElementById("toastContainer");

if (toastTrigger && toastContainer) {
  toastTrigger.addEventListener("click", () => {
    // Create a unique ID for each toast
    const toastId =
      "toast-" + Date.now() + "-" + Math.floor(Math.random() * 1000);
    const alertId =
      "alert-" + Date.now() + "-" + Math.floor(Math.random() * 1000);
    const d = new Date();
    let time = d.getDate();
    let year = d.getFullYear();
    let month = d.getMonth() + 1;
    let hour = d.getHours();
    let minutes = d.getMinutes();
    let seconds = d.getSeconds();
    // Toast HTML
    let alertHTML = "";
    const toastHTML = `
      <div class="toast hiddenmed " id="${toastId}" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
          
          <strong class="me-auto">Aple</strong>
          <small class="text-body-secondary">${time}/${month}/${year} ${hour}:${minutes}:${seconds}</small>
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">Your username or password is incorrect. If you don't have an account, please sign up on the signup page.</div>
      </div>
    `;

    // Insert the toast into the container
    toastContainer.insertAdjacentHTML("beforeend", toastHTML);

    // Get the new toast element and show it
    const newToast = document.getElementById(toastId);
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(newToast);
    toastBootstrap.show();

    // Optionally, remove the toast from DOM after it hides
    newToast.addEventListener("hidden.bs.toast", () => {
      newToast.remove();
    });
    if (window.innerWidth <= 767) {
      let red = Math.random() * 255;
      let blue = Math.random() * 255;
      let green = Math.random() * 255;
      let alertHTML = "";
      if ((red + blue + green) / 3 < 150) {
        alertHTML = `
      <div class="alert showsm  alertbg" id="${alertId}" role="alert" >
        Your username or password is incorrect. If you don't have an account, please <a class="alert-link">Sign Up</a> here.
      </div>
    `;
      } else {
        alertHTML = `
      <div class="alert showsm gray" id="${alertId}" role="alert" style="background-color:rgb(${red}, ${blue}, ${green});">
        Your username or password is incorrect. If you don't have an account, please <a class="alert-link">Sign Up</a> here.
      </div>
    `;
      }
      // Insert the alert into the container
      alertContainer.insertAdjacentHTML("beforeend", alertHTML);

      // Get the new alert element
      const newalert = document.getElementById(alertId);

      // Optionally, remove the alert from DOM after a timeout
      setTimeout(() => {
        if (newalert) newalert.remove();
      }, 4000);
    }
  });
}

/* <img src="/static/images/viruslogo.png" class="rounded me-2" alt="..." />; */
