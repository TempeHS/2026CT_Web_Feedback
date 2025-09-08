# Connor.K Web Design Project Feedback

## Page & Component Summary Table

| Page Name          | Bootstrap Components Used                                                                      | Flask/Jinja2 Functionality                            |
| ------------------ | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| index.html         | Grid, Card, Button, Container, Row, Carousel (slider), Responsive columns, Progress bar, Toast | extends, include, for loop, variable rendering, block |
| contact.html       | Grid, Responsive columns, Container, Row, Iframe                                               | extends, block                                        |
| layout.html        | Navbar, Container, Progress bar, Toast                                                         | block, include                                        |
| articlelayout.html | Container, Bootstrap CSS/JS includes                                                           | include, block                                        |
| credits.html       | Grid, Container, Row, Responsive columns (col-lg-6, col-md-8, col-sm-12)                       | extends, block                                        |
| flash.html         | None (custom CSS only)                                                                         | None (standalone CSS)                                 |
| goodweb.html       | Grid, Container, Row, Responsive columns (col-lg-6, col-md-8, col-sm-12)                       | extends, block                                        |
| loginpage.html     | Grid, Container, Row, Responsive columns (col-sm-12, col-md-8, col-lg-6)                       | extends, include, block                               |
| starting.html      | Grid, Container, Row, Responsive columns, Hidden utility (hidden-md)                           | extends, include, block                               |

---

## HTML Structure & Semantics

**Strengths:**

- Good use of semantic HTML5 elements and Bootstrap grid for layout.
- Template inheritance with `layout.html` and use of partials for reusable components.
- Jinja2 blocks and includes are used appropriately for structure.

**Areas for Improvement:**

- Consider adding more ARIA attributes and alt text for images to improve accessibility.
- Ensure all forms and interactive elements are properly labeled for screen readers.

---

## CSS Design & Styling

**Strengths:**

- Custom styles for navbar, cards, progress bar, and toast notifications enhance visual appeal.
- Bootstrap is used effectively for layout and responsive design.
- Consistent color scheme and spacing.

**Areas for Improvement:**

- Explore more advanced CSS features such as transitions or hover effects for interactivity.
- Organize custom CSS into sections with comments for easier maintenance.

---

## Flask Implementation

**Strengths:**

- Well-structured routes for each page, clearly defined in `main.py`.
- Data passed to templates using Jinja2 for loops and variable rendering.
- Logical separation of concerns between backend and frontend.

**Areas for Improvement:**

- Add error handling for invalid routes or missing data.
- Consider implementing form validation for user input on login or contact pages.

---

## User Experience & Functionality

**Strengths:**

- Intuitive navigation with menu partial and clear page structure.
- Interactive features like progress bar, toast notifications, and slider enhance engagement.
- Content is well-organized and easy to follow.

**Areas for Improvement:**

- Add more interactive elements, such as modals or tooltips, to further improve usability.
- Ensure all links and buttons are clearly labeled and accessible.

---

## Technical Implementation

**Strengths:**

- Multiple unique pages and features implemented, including custom scripts and partials.
- Efficient file organization with separate folders for CSS, JS, images, and templates.
- Good use of template inheritance and reusable components.

**Areas for Improvement:**

- Document custom scripts and components for easier future updates.
- Review file naming conventions for consistency.

---

# Feedback Template

## Page & Component Summary Table

## File Analysis Summary

## HTML Structure and Semantics

## CSS Design and Styling

## Flask Implementation

## User Experience and Functionality

## Technical Implementation
