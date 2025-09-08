# Khoi.C Web Design Project Feedback

## Page & Component Summary Table

| Page Name             | Bootstrap Components Used                                        | Flask/Jinja2 Functionality                            |
| --------------------- | ---------------------------------------------------------------- | ----------------------------------------------------- |
| index.html            | Grid, Card, Button, Container, Row, Carousel, Responsive columns | extends, include, for loop, variable rendering, block |
| contact.html          | Grid, Responsive columns, Container, Row, Form, Card             | extends, block                                        |
| layout.html           | Navbar, Container                                                | block, include                                        |
| pricing.html          | Grid, Card, Button, Container                                    | extends, block                                        |
| about_laptops.html    | Grid, Card, Container                                            | extends, block                                        |
| about_desktops.html   | Grid, Card, Container                                            | extends, block                                        |
| find_laptops.html     | Grid, Card, Container                                            | extends, block                                        |
| find_desktops.html    | Grid, Card, Container                                            | extends, block                                        |
| compare_student.html  | Grid, Table, Container                                           | extends, block                                        |
| compare_employee.html | Container, Typography utilities (d-flex, justify-content-center) | extends, block                                        |
| login.html            | Form, Form-group, Form-control, Container, Responsive columns    | extends, block                                        |
| signup.html           | Form, Form-group, Form-control, Container, Responsive columns    | extends, block                                        |
| compare_employee.html | Grid, Table, Container                                           | extends, block                                        |
| login.html            | Form, Card, Container                                            | extends, block                                        |
| signup.html           | Form, Card, Container                                            | extends, block                                        |
| partials/menu.html    | Navbar, Menu                                                     | include                                               |

---

## HTML Structure and Semantics

Khoi, your web design project demonstrates a solid understanding of HTML structure and semantic elements. You have organized your templates well, using base templates and partials to keep your code clean and maintainable. The use of semantic tags and template inheritance with Jinja2 blocks helps make your site accessible and easy to update. For future improvement, consider adding more ARIA attributes and descriptive alt text to images to further enhance accessibility.

## CSS Design and Styling

Your CSS is well-organized, and you have made good use of Bootstrap components for layout and styling. The custom styles for fonts, navbar branding, menu backgrounds, and carousel images show creativity and attention to detail. Responsive design is implemented effectively, making your site usable on different devices. To take your styling further, experiment with custom color schemes and transitions to give your site a unique look and feel.

## Flask Implementation

Your Flask application is well-structured, with clear routes for each page and logical separation of templates. You use Jinja2 features like loops and includes to render dynamic content, which is excellent for a first web project. Error handling and validation could be improved by adding feedback for invalid form submissions and handling missing data gracefully. Try adding more comments to your Python code to explain your logic and help future development.

## User Experience and Functionality

Navigation across your web design project is intuitive, and the use of interactive features like sliders and forms adds value for users. Content is well-organized, and the inclusion of comparison pages and pricing information makes your site informative. For further improvement, consider adding confirmation messages for form submissions and interactive elements such as tooltips or modals to guide users through your site.

## Technical Implementation

You have developed a comprehensive web design project with many unique pages and features, including comparison tools and authentication forms. Your project structure is efficient, with assets and templates organized in logical folders. To further enhance your technical skills, try implementing user authentication or saving form data to a database. This will help you build even more interactive and useful web applications in the future.
