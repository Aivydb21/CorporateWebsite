const newseletter = document.getElementById("newsletter-wrapper");
const newsletterBtn = document.getElementById("newsletter-submit-btn");
const newseletterAlert = document.getElementById("newsletter-alert");
const form = document.getElementById("newsletter-form");

const pathname = window.location.pathname;

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  const inputField = document.getElementById("newsletter-input-field");
  const alertEl = document.createElement("div");
  alertEl.className =
    "alert mt-3 d-flex align-items-center justify-content-between showAlert";
  alertEl.innerText = "Newsletter subscribed successfully!";

  const sendData = async () => {
    const formData = new FormData();
    formData.append("email", inputField.value);
    const headers = {
      "X-CSRFToken": token,
    };

    if (inputField.value.length > 0) {
      const response = await fetch(pathname, {
        method: "POST",
        mode: "same-origin",
        body: formData,
        headers,
      });

      if (response.status === 200) {
        alertEl.classList.add("alert-success");
        newsletterBtn.setAttribute("disabled", true);
        newseletter.appendChild(alertEl);
        inputField.value = "";
      } else {
        alertEl.classList.add("alert-danger");
        newseletter.appendChild(alertEl);
      }
    }
  };

  sendData();

  setTimeout(() => {
    newseletter.removeChild(alertEl);

    newsletterBtn.removeAttribute("disabled");
  }, 2000);
});
