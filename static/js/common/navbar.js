const menuBtn = document.getElementById("hamburger-btn");
const closeBtn = document.getElementById("drawer-close-btn");
const drawer = document.getElementById("nav-drawer");
const navbar = document.getElementById("navbar");
const footerText = document.getElementById('footer-text-info');

const toggleDrawer = () => {
  if (drawer.classList.contains("showDrawer")) {
    drawer.classList.remove("showDrawer");
  } else {
    drawer.classList.add("showDrawer");
  }
};

menuBtn.addEventListener("click", toggleDrawer);
closeBtn.addEventListener("click", toggleDrawer);

document.addEventListener("scroll", () => {
  if (window.scrollY > 60) {
    navbar.className = "fixed";
  } else {
    navbar.className = "";
  }
});

if (footerText?.innerText?.length > 200) {
  const formatedString = `${footerText?.innerText?.slice(0, 200)}...`;

  footerText.innerText = formatedString;
}
