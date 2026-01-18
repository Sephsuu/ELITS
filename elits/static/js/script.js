window.addEventListener('scroll', reveal)
    function reveal(){
        var reveals = document.querySelectorAll('.reveal');
        for(var i = 0; i < reveals.length; i++){
            var wh = window.innerHeight;
            var rt = reveals[i].getBoundingClientRect().top;
            var rp = 150;

            if(rt < wh - rp){
                reveals[i].classList.add('active');
            }else{
                reveals[i].classList.remove('active');
            }
        }
    }

    window.addEventListener('scroll', revealLeft)
    function revealLeft(){
        var reveals = document.querySelectorAll('.reveal-left');
        for(var i = 0; i < reveals.length; i++){
            var wh = window.innerHeight;
            var rt = reveals[i].getBoundingClientRect().top;
            var rp = 150;

            if(rt < wh - rp){
                reveals[i].classList.add('active');
            }else{
                reveals[i].classList.remove('active');
            }
        }
    }

    window.addEventListener('scroll', revealRight)
    function revealRight(){
        var reveals = document.querySelectorAll('.reveal-right');
        for(var i = 0; i < reveals.length; i++){
            var wh = window.innerHeight;
            var rt = reveals[i].getBoundingClientRect().top;
            var rp = 150;

            if(rt < wh - rp){
                reveals[i].classList.add('active');
            }else{
                reveals[i].classList.remove('active');
            }
        }
    }

    // document.addEventListener("DOMContentLoaded", function() {
    //     const images = [
    //         "images/jp.png",
    //         "images/elits-1st-year-rep2.png",
    //         "images/president.png"
    //         // Add more image paths as needed
    //     ];
    
    //     const elitsMemberImg = document.getElementById("elitsMemberImg");
    
    //     function changeImage() {
    //         const randomIndex = Math.floor(Math.random() * images.length);
    //         elitsMemberImg.classList.add('fade-out');
    
    //         setTimeout(() => {
    //             elitsMemberImg.src = images[randomIndex];
    //             elitsMemberImg.classList.remove('fade-out');
    //         }, 500); // Match the timeout duration with the CSS transition duration
    //     }
    
    //     // Change image on page load
    //     changeImage();
    
    //     // Change image on click
    //     elitsMemberImg.addEventListener("click", changeImage);
    // });

    document.addEventListener("DOMContentLoaded", function() {
        const searchInput = document.getElementById("searchInput");
        const dropdown = document.getElementById("dropdown");
    
        const sections = [
            { id: "index.html#history-section", name: "ELITS History" },
            { id: "index.html#awards-section", name: "ELITS Awards/Achievements" },
            { id: "index.html#news-section", name: "News/Latest News" },
            { id: "index.html#events-section", name: "Events/Latest Events" },
            { id: "index.html#join", name: "Join the Organization/Open Positions" },
            { id: "index.html#footer", name: "Contacts/Footer" },
            { id: "shop.html", name: "ELITS Membership" },
            { id: "shop.html#merchandise-section", name: "ELITS Merchandise/Shop" },
            { id: "who-are-we.html", name: "ELITS Overview" },
            { id: "shop.html#elits-members", name: "ELITS Officers" },
            { id: "dev.html", name: "About the Developer" },
        ];
    
        searchInput.addEventListener("input", function() {
            const query = searchInput.value.toLowerCase();
            const matches = sections.filter(section => section.name.toLowerCase().includes(query));
            updateDropdown(matches, query);
        });
    
        function updateDropdown(matches, query) {
            dropdown.innerHTML = "";
            if (query === "") {
                dropdown.classList.add("hidden");
                return;
            }
    
            if (matches.length === 0) {
                const noResultDiv = document.createElement("div");
                noResultDiv.className = "dropdown-item";
                noResultDiv.textContent = "No results found";
                dropdown.appendChild(noResultDiv);
            } else {
                matches.forEach(match => {
                    const div = document.createElement("div");
                    div.className = "dropdown-item";
                    div.innerHTML = highlightText(match.name, query);
                    div.addEventListener("click", () => {
                        if (match.id.includes('.html')) {
                            window.location.href = match.id;
                        } else {
                            document.getElementById(match.id).scrollIntoView({ behavior: "smooth", block: "start" });
                        }
                        dropdown.classList.add("hidden");
                    });
                    dropdown.appendChild(div);
                });
            }
    
            dropdown.classList.remove("hidden");
        }
    
        function highlightText(text, query) {
            const regex = new RegExp(query, 'gi');
            return text.replace(regex, match => `<span class="highlight">${match}</span>`);
        }
    
        document.addEventListener("click", (event) => {
            if (!event.target.closest("#searchInput") && !event.target.closest("#dropdown")) {
                dropdown.classList.add("hidden");
            }
        });
    });
    
    