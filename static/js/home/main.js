const servicesDescription = document.getElementsByClassName(
  "services-card-description"
);
const missionDescription = document.getElementsByClassName(
  "mission-description"
);

const heroContSwiper = new Swiper(".heroSwiperSlider", {
  direction: "horizontal",

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  autoplay: {
    delay: 5000,
  },
});

const missionValuesContSwiper = new Swiper(".swiperMissionValuesContainer", {
  direction: "horizontal",
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
  },

  // Navigation arrows
  navigation: {
    nextEl: ".mission-button-next",
    prevEl: ".mission-button-prev",
  },

  autoplay: {
    delay: 5000,
  },
});

const servicesCardsContSwiper = new Swiper(".servicesSwiperContainer", {
  slidesPerView: 3,
  spaceBetween: 30,
  pagination: false,
  direction: "horizontal",
  loop: true,
  autoplay: {
    delay: 5000,
  },
  navigation: {
    nextEl: ".services-button-next",
    prevEl: ".services-button-prev",
  },

  breakpoints: {
    0: {
      slidesPerView: 1,
      spaceBetween: 30,
    },

    570: {
      slidesPerView: 1,
      spaceBetween: 30,
    },

    768: {
      slidesPerView: 2,
      spaceBetween: 30,
    },

    991: {
      slidesPerView: 3,
      spaceBetween: 30,
    },
  },
});

for (let i = 0; i < servicesDescription.length; i++) {
  if (servicesDescription[i].innerText.length > 210) {
    const formatedText = `${servicesDescription[i].innerText?.slice(
      0,
      210
    )}...`;

    servicesDescription[i].innerText = formatedText;
  }
}

for (let i = 0; i < missionDescription.length; i++) {
  if (missionDescription[i].innerText.length > 1200) {
    const formatedText = `${missionDescription[i].innerText?.slice(
      0,
      1200
    )}...`;

    missionDescription[i].innerText = formatedText;
  }
}

// newsletterBtn.addEventListener("click", (e) => {
//   const alertEl = document.createElement("div");
//   alertEl.className =
//     "alert alert-success mt-3 d-flex align-items-center justify-content-between showAlert";
//   alertEl.innerText = "Newsletter subscribed successfully!";

//   newsletterBtn.setAttribute("disabled", true);

//   newseletter.appendChild(alertEl);

//   setTimeout(() => {
//     newseletter.removeChild(alertEl);

//     newsletterBtn.removeAttribute("disabled");
//   }, 2000);
// });
