document.addEventListener('DOMContentLoaded', () => {
  const toc = document.querySelector('[data-md-component="toc"]')
  if (!toc) return

  // After every scroll-spy update, if URL has a hash, force its TOC item active
  const observer = new MutationObserver(() => {
    const hash = decodeURIComponent(location.hash)
    if (!hash) return
    const clicked = toc.querySelector(`a[href="${hash}"]`)
    if (!clicked) return
    if (!clicked.classList.contains('md-nav__link--active')) {
      toc.querySelectorAll('.md-nav__link--active').forEach(el => el.classList.remove('md-nav__link--active'))
      clicked.classList.add('md-nav__link--active')
    }
  })
  observer.observe(toc, { attributes: true, subtree: true, attributeFilter: ['class'] })
})
