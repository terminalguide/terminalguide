"use strict";

for (let headerCell of document.querySelectorAll('.list-table th[data-impl]')) {
    headerCell.addEventListener('click', function(event) {
        let impl = event.currentTarget.dataset.impl;
        for (let td of document.querySelectorAll('.list-table td[data-impl]')) {
            if (td.dataset.impl != impl) {
                td.classList.remove('highlight');
            }
        }
        for (let td of document.querySelectorAll('.list-table td[data-impl=' + impl + ']')) {
            td.classList.toggle('highlight');
        }
    });
}
