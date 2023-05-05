// index.js
async function fetchData() {
    const response = await fetch('http://localhost:8000/api/data/');
    const data = await response.json();
    const dataList = document.getElementById('data-list');
    data.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = item.content;
        dataList.appendChild(listItem);
    });
}

fetchData();
