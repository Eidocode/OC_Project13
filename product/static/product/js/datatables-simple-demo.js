window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }

    const dataTableIndex = document.getElementById('dataTableIndex');
    if (dataTableIndex) {
        new simpleDatatables.DataTable(dataTableIndex, {
            searchable: false,
            perPager: 5,
            perPageSelect: false,
        });
    }
});
