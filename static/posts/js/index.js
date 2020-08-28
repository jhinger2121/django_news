"use static";
window.onload = function () {
    // adds icon when hover on title name
    document.querySelectorAll('.post-title').forEach(element => {
        element.addEventListener('mouseenter', () => {
            element.nextElementSibling.classList.add('i-fake');
        })
        element.addEventListener('mouseleave', () => {
            element.nextElementSibling.classList.remove('i-fake');
        })
    })

    // not useful because page will refresh and active class will not change
    let secondaryNav = document.getElementById('secondary-nav')
    secondaryNav.querySelectorAll('.nav-link').forEach(element => {
        element.addEventListener('click', (e) => {
            // e.preventDefault()
            let recentLink = secondaryNav.getElementsByClassName('active-s')[0];
            recentLink.classList.remove('active-s')
            e.target.classList.add('active-s')

            // let url = 'https://api.github.com/repos/javascript-tutorial/en.javascript.info/commits'
            // fetch(url)
            // .then((resp) => resp.json())
            // .then(function(data){
            //     console.log(data[0])
            // })
        })
    })
}