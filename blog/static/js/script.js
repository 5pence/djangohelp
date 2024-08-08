const hoverEle = document.getElementById('stupidJs');

function addHoverStyle() {
    hoverEle.style.backroundColor = 'orange'
    hoverEle.style.color = 'white'
}

function removeHoverStyle() {
    hoverEle.style.backroundColor = 'white'
    hoverEle.style.color = 'black'
}
hoverEle.addEventListener('mouseenter', addHoverStyle);
hoverEle.addEventListener('mouseleave', removeHoverStyle);