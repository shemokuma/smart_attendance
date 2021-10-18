
const tabs=document.querySelectorAll('[data-target]'),
      tabContents=document.querySelectorAll('[data-toggle]')
tabs.forEach(tab =>{
  tab.addEventListener('click',()=>{
    const target=document.querySelector(tab.dataset.target)
    tabContents.forEach(tabContent =>{
      tabContent.classList.remove('modal')
    })
    target.classList.add('modal');
    tabs.forEach(tab=>{
      tab.classList.remove('modal')
    })
    tab.classList.add('modal')
  })
})