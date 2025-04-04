document.addEventListener("mousemove", (e) => {
    let trail = document.createElement("div");
    trail.classList.add("trail");
    document.body.appendChild(trail);
    trail.style.left = `${e.clientX}px`;
    trail.style.top = `${e.clientY}px`;
  
    setTimeout(() => {
      trail.remove();
    }, 500);
  });
  