const bg = document.getElementById('h');
window.addEventListener('scroll',
    function () {
        bg.style.backgroundSize = Math.round(110 + window.pageYOffset / 20) + '%';
        /**/
    });