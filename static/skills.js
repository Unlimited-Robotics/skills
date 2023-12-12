function load_readme(version){
    let urlVersion = url_readme_main.replace('main', version);
    fetch(urlVersion)
    .then(response => {
        if (!response.ok) {
            if (response.status == 404) {
              return 'No README found for this version';
            }
            throw new Error(`Failed to fetch content. Status code: ${response.status}`);
        }
        return response.text();
    })
    .then(markupContent => {
      const contentDivs = document.querySelectorAll('.versions div');
      contentDivs.forEach(div => div.classList.remove('selected'));

      document.getElementById(version).classList.add('selected');
      document.getElementById('markdown-container').innerHTML = marked.parse(markupContent);
    })
    .catch(error => {
        console.error('Error:', error.message);
    });
  }

  function warn_unsafe() {
    document.getElementById('installdanger').hidden = false;
    document.getElementById('installcmd').hidden = true;
  }

  $(document).ready(function () {
    var this_vers = document.getElementById('latest-main-version').textContent.trim();
    document.getElementById(this_vers).classList.add('main');
    check_supply_chain_attack("_package_name", this_vers, warn_unsafe);
    load_readme(this_vers);
  });