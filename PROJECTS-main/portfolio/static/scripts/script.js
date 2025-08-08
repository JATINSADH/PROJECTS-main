// ========================================= toggle Icon navbar =============================

let newIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

newIcon.onclick = () => {
    newIcon.classList.toggle('fa-xmark');
    navbar.classList.toggle('active');
}

// ========================================= scroll section active link =============================

let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        }
    });

// ========================================= sticky navbar =============================
    let header = document.querySelector('header');
    header.classList.toggle('sticky', window.scrollY > 100);

// ========================================= remove toggle icon and navbar =============================
    newIcon.classList.remove('fa-xmark');
    navbar.classList.remove('active');
};


// ========================================= scroll reveal =============================

ScrollReveal({
    distance: '80px',
    duration: 2000,
    delay: 200,
});

ScrollReveal().reveal('.home-content, heading', { origin: 'top' });
ScrollReveal().reveal('.home-img, .services-container, .project-box, .contact form',  { origin: 'buttom' });
ScrollReveal().reveal('.home-contact h1, .about-img', { origin: 'left' });
ScrollReveal().reveal('.home-contact p, .about-content', { origin: 'right' });

// ========================================= typed js =============================

const typed = new Typed('.multiple-text', {
    strings: ["Student.>", "AIML-Engineer.>","Programmer.>","Developer.>"],
    typeSpeed: 70,
    backSpeed: 70,
    backDelay: 1000,
    loop: true,
});

var typedAbout = new Typed(".about-multiple-text", {
    strings: ["Student.>", "Programmer.>", "Problem Solver.>","AIML-Engineer.>"], // About section ke liye text
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});

// ========================================= Mouse Move =============================

document.addEventListener('mousemove', function(event) {
    const glitter = document.createElement('div');
    glitter.className = 'glitter';

    // Set the position of the glitter
    glitter.style.left = `${event.pageX}px`;
    glitter.style.top = `${event.pageY}px`;

    // Append the glitter to the body
    document.body.appendChild(glitter);

    // Add logic to remove the glitter after a short delay
    setTimeout(() => {
        glitter.remove();
    }, 500); // Adjust the delay as per your requirement
});
