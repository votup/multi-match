/* Sections */
const header = document.querySelector('header'),
      main = document.querySelector('main'),
      footer = document.querySelector('footer')

/* Set Main top margin */
if (main) {
  let headerHeight = header.clientHeight
  main.style.marginTop = headerHeight + "px"
}

/* Sticky Footer */
if (footer) {
  let footerHeight = footer.clientHeight
  main.style.minHeight = "calc(100vh - " + footerHeight + "px)"
}