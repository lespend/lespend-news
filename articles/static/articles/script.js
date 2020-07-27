// Hadle Search Button
const searchButton = document.getElementsByClassName('page-header__search-button')[0];
searchButton.onclick = function() {
    const searchPopup = document.getElementsByClassName('search-popup')[0];
    searchPopup.style.display = 'block';
};

const searchCloseButton = document.getElementsByClassName('search-popup__close')[0];
searchCloseButton.onclick = function() {
    const searchPopup = document.getElementsByClassName('search-popup')[0];
    searchPopup.style.display = 'none';
};


// Hadle Menu Button
const menuButton = document.getElementsByClassName('page-header__menu-button')[0];
console.log(menuButton);
menuButton.onclick = function() {
    console.log(1);
    const nav = document.getElementsByClassName('page-header__navigation')[0];
    console.log(nav);
    nav.classList.add('page-header__navigation--show');
};

const menuCloseButton = document.getElementsByClassName('page-header__menu-close-button')[0];
menuCloseButton.onclick = function() {
    const nav = document.getElementsByClassName('page-header__navigation')[0];
    nav.classList.remove('page-header__navigation--show');
};
