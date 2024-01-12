// script.js 

document.addEventListener('DOMContentLoaded', function () { 
	const navbarLinks = 
		document.querySelectorAll('nav ul li a'); 
	const sections = 
		document.querySelectorAll('.section');

	window.addEventListener('scroll', function () { 
		const currentPos = window.scrollY; 

		sections.forEach(function (section) { 
			const sectionTop = section.offsetTop - 80; 
			const sectionHeight = section.offsetHeight; 
			const sectionId = section.getAttribute('id'); 

			if (currentPos >= sectionTop && 
				currentPos < sectionTop + sectionHeight) { 
				navbarLinks.forEach(function (navbarLink) { 
                    // If section is not visible
					navbarLink.classList.remove('ring', 'bg-hoverColor/10', 'font-medium', 'md:bg-primaryColor/10', 'md:text-primaryColor', 'md:outline-primaryColor');
					navbarLink.classList.add('bg-transparent', 'max-sm:text-yellowWhite/70', 'md:hover:text-yellowWhite/70', 'md:hover:bg-yellowWhite/10', 'md:outline-transparent');
				}); 

                // Section is visible
				document.querySelector('nav ul li a[href="#'
					+ sectionId + '"]') 
				.classList.add('ring', 'bg-hoverColor/10', 'font-medium', 'md:bg-primaryColor/10', 'md:text-primaryColor', 'md:outline-primaryColor');

                document.querySelector('nav ul li a[href="#'
					+ sectionId + '"]') 
				.classList.remove('bg-transparent', 'max-sm:text-yellowWhite/70', 'md:hover:text-yellowWhite/70', 'md:hover:bg-yellowWhite/10', 'md:outline-transparent');
			} 
		}); 
	}); 
});
