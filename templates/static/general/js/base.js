document.addEventListener("DOMContentLoaded", function(event) {

const showNavbar = (toggleId, navId, bodyId, headerId) =>{
const toggle = document.getElementById(toggleId),
nav = document.getElementById(navId),
bodypd = document.getElementById(bodyId),
headerpd = document.getElementById(headerId)

    const formNavDiv = document.querySelector(".FormNavDiv")

if(toggle && nav && bodypd && headerpd){
toggle.addEventListener('click', ()=>{

    const  left = window.getComputedStyle(formNavDiv).getPropertyValue('left')



 left  === "100px"?  formNavDiv.style.left = "240px" :   formNavDiv.style.left = "100px"

nav.classList.toggle('show')

toggle.classList.toggle('bx-x')

bodypd.classList.toggle('body-pd')

headerpd.classList.toggle('body-pd')
})
}
}

showNavbar('header-toggle','nav-bar','body-pd','header')


const linkColor = document.querySelectorAll('.nav_link')

function colorLink(){
if(linkColor){
linkColor.forEach(l=> l.classList.remove('active'))
this.classList.add('active')
}
}
linkColor.forEach(l=> l.addEventListener('click', colorLink))


});



$(document).ready(function () {


    $('#example').DataTable({
        layout: {
            topStart: 'buttons',
               top2Start: 'pageLength'
        },
                buttons: [
                    {extend: 'copy', className: 'copyButton', text: "<img width=\"30\" height=\"30\" src=\"https://img.icons8.com/ios/50/copy--v1.png\" alt=\"copy--v1\"/>", title: "copiar"},
                    {extend: 'excel', className: 'excelButton' ,text: "<svg xmlns=\"http://www.w3.org/2000/svg\" x=\"0px\" y=\"0px\" width=\"30\" height=\"30\" viewBox=\"0 0 48 48\">\n" +
                            "<path fill=\"#4CAF50\" d=\"M41,10H25v28h16c0.553,0,1-0.447,1-1V11C42,10.447,41.553,10,41,10z\"></path><path fill=\"#FFF\" d=\"M32 15H39V18H32zM32 25H39V28H32zM32 30H39V33H32zM32 20H39V23H32zM25 15H30V18H25zM25 25H30V28H25zM25 30H30V33H25zM25 20H30V23H25z\"></path><path fill=\"#2E7D32\" d=\"M27 42L6 38 6 10 27 6z\"></path><path fill=\"#FFF\" d=\"M19.129,31l-2.411-4.561c-0.092-0.171-0.186-0.483-0.284-0.938h-0.037c-0.046,0.215-0.154,0.541-0.324,0.979L13.652,31H9.895l4.462-7.001L10.274,17h3.837l2.001,4.196c0.156,0.331,0.296,0.725,0.42,1.179h0.04c0.078-0.271,0.224-0.68,0.439-1.22L19.237,17h3.515l-4.199,6.939l4.316,7.059h-3.74V31z\"></path>\n" +
                            "</svg>", title: "exportar Excel"},
                    {extend: 'pdf', className: 'pdfButton', text: "<img width=\"30\" height=\"30\" src=\"https://img.icons8.com/papercut/60/pdf.png\" alt=\"pdf\"/>", title: "baixar PDF"},
                    {extend: 'print', className: 'printButton' ,text: "<img width=\"30\" height=\"30\" src=\"https://img.icons8.com/ios-filled/50/print.png\" alt=\"print\"/>", title: "Imprimir documento", }
                ],




    });


});