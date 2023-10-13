const headerBtn = document.querySelectorAll('.header-btn')
const resDiv = document.querySelectorAll('.res-div')
const btns = document.querySelectorAll('.btn')

document.addEventListener('DOMContentLoaded', function () {
    headerBtn.forEach(button => {
        button.addEventListener('mouseover', () => {
            button.style.backgroundColor = '#888';
            button.style.padding = '15px 10px 10px 5px';
        });

        button.addEventListener('mouseout', () => {
            button.style.backgroundColor = '#666666';
            button.style.padding = '0 10px 10px 5px';
        });
    });

    resDiv.forEach(element => {
        element.addEventListener('mouseover', () => {
            element.style.boxShadow = '0 0 20px rgba(0, 0, 0, 0.5)';
            element.style.transform = 'translate(-0.5%, -0.5%)';
        });

        element.addEventListener('mouseout', () => {
            element.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.5)';
            element.style.transform = 'translate(0, 0)';
        });
    });

    btns.forEach(button => {
        button.addEventListener('mouseover', () => {
            button.style.backgroundColor = '#666666';
        });

        button.addEventListener('mouseout', () => {
            button.style.backgroundColor = '#222222';
        });
    });
});
