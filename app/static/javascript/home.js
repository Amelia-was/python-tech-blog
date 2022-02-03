document.addEventListener('scroll', function(e) {
    let header = document.querySelector('header');
    if (window.scrollY > 0) {
        header.classList.add('box-shadow');
    }
    else {
        header.classList.remove('box-shadow');
    }
});