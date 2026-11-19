const navigation = Array.from(document.querySelectorAll('nav a'));
const sections = navigation.map(link => document.querySelector(link.hash));
const pageHeader = document.querySelector('.site-head');

function updateReadingPosition() {
  const offset = pageHeader.getBoundingClientRect().bottom + 30;
  const remaining = document.documentElement.scrollHeight - innerHeight;
  let current = sections[0];
  for (const section of sections) {
    if (section.getBoundingClientRect().top <= offset) current = section;
  }
  if (remaining > 0 && scrollY >= remaining - 2) current = sections.at(-1);
  for (const link of navigation) {
    if (link.hash === '#' + current.id) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
  pageHeader.style.setProperty('--progress', remaining > 0 ? Math.min(1, scrollY / remaining) : 1);
}

addEventListener('scroll', updateReadingPosition, { passive: true });
addEventListener('resize', updateReadingPosition);
updateReadingPosition();

const copyButton = document.querySelector('#copy');
const citation = document.querySelector('#bibtex');
if (navigator.clipboard && navigator.clipboard.writeText) {
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    const status = document.querySelector('#copy-status');
    try {
      await navigator.clipboard.writeText(citation.textContent);
      copyButton.textContent = 'Copied';
      status.textContent = 'Citation copied to clipboard.';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(citation);
      const selection = getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      copyButton.textContent = 'Use system copy';
      status.textContent = 'Citation selected. Use your device’s copy command.';
    }
  });
}
