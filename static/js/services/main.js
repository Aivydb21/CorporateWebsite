const serviceDescription = document.getElementsByClassName(
  "service-description"
);

for (let i = 0; i < serviceDescription.length; i++) {
  if (serviceDescription[i].innerText.length > 500) {
    const formatedText = `${serviceDescription[i].innerText.slice(0, 500)} ...`;

    serviceDescription[i].innerText = formatedText;
  }
}
