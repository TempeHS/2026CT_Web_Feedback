# Daniel.SDLF Web Design Project Feedback

## Page & Component Summary Table

| Page Name     | Bootstrap Components Used                                                 | Flask/Jinja2 Functionality                            |
| ------------- | ------------------------------------------------------------------------- | ----------------------------------------------------- |
| index.html    | Grid, Card, Button, Container, Row, Carousel (slider), Responsive columns | extends, include, for loop, variable rendering, block |
| contacts.html | Grid, Responsive columns, Container, Row                                  | extends, block                                        |
| layout.html   | Navbar, Container                                                         | block, include                                        |
| RAC.html      | Container, Grid, Row, Typography utilities                                | extends, block                                        |
| TTHP.html     | Container, Grid, Row, Typography utilities                                | extends, block                                        |
| WG.html       | Container, Grid, Row, Typography utilities                                | extends, block                                        |

---

**Strengths:**

- Good use of semantic HTML5 elements and Bootstrap grid for layout.
- Template inheritance with `layout.html` and use of partials for reusable components.
- Jinja2 blocks and includes are used appropriately for structure.

**Areas for Improvement:**

- Add more ARIA attributes and alt text for images to improve accessibility.
- Ensure all forms and interactive elements are properly labeled for screen readers.

---

**Strengths:**

- Custom styles for navbar and carousel images add visual interest.
- Bootstrap is used effectively for layout and responsive design.
- Consistent color scheme and spacing.

**Areas for Improvement:**

- Explore more advanced CSS features such as transitions or hover effects for interactivity.
- Organize custom CSS into sections with comments for easier maintenance.

---

**Strengths:**

- Well-structured routes for each page, clearly defined in `main.py`.
- Data passed to templates using Jinja2 for loops and variable rendering.
- Logical separation of concerns between backend and frontend.

**Areas for Improvement:**

- Add error handling for invalid routes or missing data.
- Consider implementing form validation for user input on contact pages.

---

**Strengths:**

- Intuitive navigation with menu partial and clear page structure.
- Interactive features like slider and genre explorer enhance engagement.
- Content is well-organized and easy to follow.

**Areas for Improvement:**

- Add more interactive elements, such as modals or tooltips, to further improve usability.
- Ensure all links and buttons are clearly labeled and accessible.

---

**Strengths:**

- Multiple unique pages and features implemented, including custom partials and genre explorer.
- Efficient file organization with separate folders for CSS, images, and templates.
- Good use of template inheritance and reusable components.

**Areas for Improvement:**

- Document custom scripts and components for easier future updates.
- Review file naming conventions for consistency.

---
