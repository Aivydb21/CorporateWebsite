const dropdownItem = document.getElementsByClassName("item");
const dropdownList = document.getElementById("country-list");
const selectField = document.getElementById("country-select-input");
const contactForm = document.getElementById("contact-form");
const formContainer = document.getElementById("contact-form-container");

const firstName = document.getElementsByName("first_name")[0];
const lastName = document.getElementsByName("last_name")[0];
const email = document.getElementsByName("email")[0];
const phone = document.getElementsByName("phone_number")[0];
const queryType = document.getElementsByName("query_type")[0];
const message = document.getElementsByName("message")[0];
const token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

const fetchCountries = async () => {
  const countriesData = await fetch(
    "https://restcountries.com/v2/all?fields=name,flag,callingCodes"
  )
    .then((resp) => resp.json())
    .then((data) => data);

  [...countriesData].forEach((item) => {
    const optionItem = document.createElement("option");

    optionItem.value = item.callingCodes[0];
    optionItem.innerText = `${item.name} +${item.callingCodes[0]}`;

    optionItem.setAttribute("data-code", item.callingCodes[0]);

    selectField.appendChild(optionItem);
  });
};

fetchCountries();

contactForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const alertEl = document.createElement("div");
  alertEl.className = "alert alert-success my-3";
  alertEl.innerText = "Form submitted successfully!";

  const formData = new FormData();
  formData.append("first_name", firstName.value);
  formData.append("last_name", lastName.value);
  formData.append("email", email.value);
  formData.append("phone_number", phone.value);
  formData.append("query_type", queryType.value);
  formData.append("message", message.value);

  const sendData = async () => {
    const resp = await fetch("/contact/", {
      body: formData,
      headers: {
        "X-CSRFToken": token,
      },
      method: "POST",
      mode: "same-origin",
    });

    if (resp.status === 200) {
      contactForm.reset();
      formContainer.appendChild(alertEl);
    } else {
      alert("Something went wrong!");
    }
  };

  sendData();

  setTimeout(() => {
    formContainer.removeChild(alertEl);
  }, 2000);
});
