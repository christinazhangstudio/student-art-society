const observer = new IntersectionObserver(f, {
    threshold:[0,1]
  });
  
  function f(entries) {
    for (const entry of entries) {
      if (entry.isIntersecting && entry.intersectionRatio >= 1) {
          entry.target.classList.toggle("inbound", true)
      }
      else {
        if(!entry.target.classList.contains("expanded")) {
          entry.target.classList.toggle("inbound", false)
        }
      }
    }
  }
  
  const itemEls = Array.from(document.querySelectorAll(".gallery-img"));
  for (const itemEl of itemEls) {
    observer.observe(itemEl)
    itemEl.addEventListener('click', function(){ this.classList.toggle("expanded");}); 
  }