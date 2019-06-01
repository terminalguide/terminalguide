"use strict";

(function() {

let currentHighlight = '';

function highlightImpl(impl) {
    currentHighlight = impl;
    for (let td of document.querySelectorAll('.list-table td[data-impl]')) {
        if (td.dataset.impl != impl) {
            td.classList.remove('highlight');
        }
    }
    if (impl) {
        for (let td of document.querySelectorAll('.list-table td[data-impl=' + impl + ']')) {
            td.classList.add('highlight');
        }
    }
}

for (let headerCell of document.querySelectorAll('.list-table th[data-impl]')) {
    headerCell.addEventListener('click', function(event) {
        let impl = event.currentTarget.dataset.impl;
        if (currentHighlight === impl) {
            impl = '';
        }
        highlightImpl(impl);
        let state = history.state || {};
        state.impl = impl;
        history.replaceState(state, '');
    });
}

function init() {
    let state = history.state || {};
    if (state.impl) {
        highlightImpl(state.impl);
    }
}

init();

}());
