const $ = document.querySelector.bind(document)
const $$ = document.querySelectorAll.bind(document)



const tabImg = $$('.img');
const tabDot = $$('.own_dot')

tabDot.forEach((tab, index) => {
    tab.onclick = function() {
        $('.own_dot.active-own').classList.remove('active-own');
        $('.img.active').classList.remove('active')


        this.classList.add('active-own')
        tabImg[index].classList.add('active')
    }
})