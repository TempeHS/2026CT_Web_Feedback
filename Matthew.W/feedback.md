# Matthew.W Web Design Project Feedback

## Page & Component Summary Table

| Page Name    | Bootstrap Components Used           | Flask/Jinja2 Functionality                     |
| ------------ | ----------------------------------- | ---------------------------------------------- |
| pricing.html | Grid, Card, Button, Container, Row  | extends, include, for loop, variable rendering |
| index.html   | Grid, Card, Button, Container, Row  | extends, include, for loop, variable rendering |
| layout.html  | Navbar, Container                   | block, include                                 |
| login.html   | Form, Button, Container, Row        | extends, block                                 |
| contact.html | Grid, Responsive columns, Container | extends, block                                 |
| tips.html    | Card, Container, Row                | extends, block                                 |

---

## HTML Structure & Semantics

**Strengths:**

- Good use of semantic HTML5 elements and Bootstrap grid for layout.
- Template inheritance with `layout.html` and use of partials for reusable components.
- Jinja2 blocks and includes are used appropriately for structure.

**Areas for Improvement:**

- Add more ARIA attributes and alt text for images to improve accessibility.
- Ensure all forms and interactive elements are properly labeled for screen readers.

**Recommendation:**
Use semantic tags and accessibility features to make the site more user-friendly for all visitors.

---

## CSS Design & Styling

**Strengths:**

- Custom styles for navbar, cards, and buttons add creativity.
- Bootstrap is used effectively for layout and responsive design.
- Consistent color scheme and spacing.

**Areas for Improvement:**

- Explore more advanced CSS features such as transitions or hover effects for interactivity.
- Organize custom CSS into sections with comments for easier maintenance.

**Recommendation:**
Try adding custom styles for buttons or cards to make the design more distinctive and personal.

---

## Flask Implementation

**Strengths:**

- Well-structured routes for each page, clearly defined in `main.py`.
- Data passed to templates using Jinja2 for loops and variable rendering.
- Logical separation of concerns between backend and frontend.

**Areas for Improvement:**

- Add error handling for invalid routes or missing data.
- Consider implementing form validation for user input on login or contact pages.

**Recommendation:**
Implement a custom 404 error page and basic input validation for future interactive features.

---

## User Experience & Functionality

**Strengths:**

- Intuitive navigation with menu partial and clear page structure.
- Interactive features like login and tips pages enhance engagement.
- Content is well-organized and easy to follow.

**Areas for Improvement:**

- Add more interactive elements, such as modals or tooltips, to further improve usability.
- Ensure all links and buttons are clearly labeled and accessible.

**Recommendation:**
Consider adding a contact form or interactive gallery to improve user engagement.

---

## Technical Implementation

**Strengths:**

- Multiple unique pages and features implemented, including custom partials and login functionality.
- Efficient file organization with separate folders for CSS, images, and templates.
- Good use of template inheritance and reusable components.

**Areas for Improvement:**

- Document custom scripts and components for easier future updates.
- Review file naming conventions for consistency.

**Recommendation:**
Continue expanding the project with new features and keep code well-documented for future development.
