function previewBeforeUpload (id) {
  const input = document.querySelector('#' + id)
  if (input) {
    input.addEventListener('change', function (e) {
      if (e.target.files.length == 0) {
        return
      }
      let file = e.target.files[0]
      let url = URL.createObjectURL(file)

      const previewDiv = document.querySelector('#' + id + '-preview div')
      if (previewDiv) {
        previewDiv.innerText = file.name
      }

      document.querySelector('#' + id + '-preview img').src = url
    })
  }
}

previewBeforeUpload('id_image')


// Remplace le contenu de la balise HTML `<option value="" selected>` par la phrase `"veuillez sélectionner une catégorie"`
function remplacerOption () {
  document.getElementsByTagName('label')[0].id = 'id_image-preview'
  document.getElementsByTagName('label')[0].innerHTML = '<img src=\'../static/images/dummy-post-square-1-thegem-blog-masonry.jpg\' alt="" width="100" height="100">'
  console.log(innerHtml)
  // Récupère l'élément select
  const select = document.querySelector("select[name='categorie']")

  // Récupère l'option par défaut
  const option = select.querySelector("option[value='']")

  // Remplace le contenu de l'option
  option.textContent = 'Veuillez sélectionner une catégorie'
}

// Écoute l'événement DOMContentLoaded
document.addEventListener('DOMContentLoaded', remplacerOption)
