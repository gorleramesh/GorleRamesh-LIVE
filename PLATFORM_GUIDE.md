# Gorle Ramesh Educational Platform - Complete Guide

## 🎯 Overview

This is a modern, Udemy-like educational platform built with HTML, CSS, and JavaScript. The platform supports multiple classes (6-10), subjects, mediums (English/Telugu), and provides an interactive learning experience with video lessons, resources, and progress tracking.

## 📁 Project Structure

```
├── landing.html              # Homepage with subject cards
├── class.html               # Main course content page
├── config/
│   ├── class6.json         # Class 6 curriculum (Updated)
│   ├── class7.json         # Class 7 curriculum
│   ├── class8.json         # Class 8 curriculum
│   ├── class9.json         # Class 9 curriculum
│   └── class10.json        # Class 10 curriculum
└── [other resource files]
```

## 🚀 Complete User Flow

### Step 1: Landing Page (`landing.html`)
- User visits the platform
- Sees Classes 6-10 with subject cards
- Each subject card displays:
  - Subject name with icon
  - Course description
  - Duration and number of chapters
  - "Explore Course" button

### Step 2: Course Selection
- User clicks "Explore Course" button
- Navigates to: `class.html?class=6&subject=Mathematics&medium=English`
- Platform loads the course content

### Step 3: Course Page (`class.html`)
#### Navbar Section
- **Logo**: Click to return to landing page
- **Subject Dropdown**: Change between available subjects
- **Medium Dropdown**: Toggle between English/Telugu

#### Course Overview
- Course title
- Full description
- Metadata:
  - Duration
  - Difficulty level
  - Rating (★)
  - Number of students

#### Video Player & Content
- Large video player (600px height)
- Current lesson title and description
- Resources section with tabs:
  - **PDF** - Download course materials
  - **HTML** - View interactive content
  - **Video** - Watch additional resources

#### Sidebar Navigation
- Collapsible chapter sections
- Lessons within each chapter
- Progress checkboxes for each lesson
- Overall progress percentage shown in header

## 📊 JSON Data Structure

### Class6.json Format

```json
[
  {
    "class": "6",
    "subject": "Mathematics",
    "courseOverview": {
      "title": "Class 6 Mathematics",
      "description": "...",
      "duration": "12 hours",
      "level": "Beginner",
      "rating": 4.8,
      "students": 1200,
      "instructor": "Gorle Ramesh"
    },
    "mediums": ["English", "Telugu"],
    "chapters": [
      {
        "chapterId": 1,
        "chapterTitle": "Geometry",
        "chapterTitleTelugu": "జ్యామితి",
        "description": "...",
        "duration": "1.5 hours",
        "lessons": [
          {
            "lessonId": 1,
            "name": "Introduction to Geometry",
            "nameTelugu": "జ్యామితికి పరిచయం",
            "description": "...",
            "duration": "15 min",
            "videoUrl": "https://www.youtube.com/embed/...",
            "resources": {
              "pdf": ["url1", "url2"],
              "html": ["url1"],
              "video": ["url1"]
            }
          }
        ],
        "resources": [
          {
            "name": "Problem Set",
            "type": "html",
            "url": "Chapter6Mat Em.html"
          }
        ]
      }
    ]
  }
]
```

## 🔧 Key Features Implemented

### 1. **Multi-Medium Support**
- Select English or Telugu from dropdown
- All lesson names display in selected language
- URL updates to reflect selection: `...&medium=Telugu`

### 2. **Subject Selection**
- Switch between subjects dynamically
- Content updates without page reload
- URL updates: `...&subject=Science`

### 3. **Course Overview Display**
- Shows comprehensive course information
- Displays metadata (duration, level, rating, students)
- Beautiful card-based layout

### 4. **Video & Resources Management**
- Embedded YouTube player
- Tabbed resource interface
- Support for PDF, HTML, and Video resources
- Direct download/view links for each resource

### 5. **Progress Tracking**
- Checkbox to mark lessons as complete
- Overall progress percentage display
- Visual progress bar in header

### 6. **Responsive Design**
- Works on desktop, tablet, and mobile
- Sidebar collapses on smaller screens
- Touch-friendly interface

## 📝 URL Parameter Reference

### Landing Page
```html
landing.html
```

### Course Page
```html
class.html?class=6&subject=Mathematics&medium=English
```

**Parameters:**
- `class` - Class number (6-10)
- `subject` - Subject name (Mathematics, Science, etc.)
- `medium` - Language (English, Telugu)

**Examples:**
- `class.html?class=6&subject=Mathematics&medium=English`
- `class.html?class=9&subject=Science&medium=Telugu`

## 🎨 Design System

### Colors
- **Primary Purple**: `#a435f0` (Udemy-inspired)
- **Dark**: `#29303b` (Text)
- **Light Gray**: `#f7f9fa` (Background)
- **Border**: `#e7e9ec` (Subtle dividers)

### Typography
- **Font**: Roboto (Google Fonts)
- **Headers**: Bold (600-700)
- **Body**: Regular (400) or Medium (500)

### Components
- Cards with hover effects
- Gradient headers (purple to pink)
- Icons from FontAwesome 6.0
- Bootstrap 4.5 grid system

## 🔄 How to Add Content

### Adding a New Chapter to Class 6
Edit `config/class6.json`:

```json
{
  "chapterId": 2,
  "chapterTitle": "Algebra",
  "chapterTitleTelugu": "బీజగణితం",
  "description": "Learn algebraic concepts",
  "duration": "2 hours",
  "lessons": [
    {
      "lessonId": 1,
      "name": "Variables and Expressions",
      "nameTelugu": "చరరాశులు మరియు సమీకరణాలు",
      "description": "...",
      "duration": "20 min",
      "videoUrl": "https://www.youtube.com/embed/...",
      "resources": {
        "pdf": [],
        "html": [],
        "video": []
      }
    }
  ]
}
```

## 📱 Browser Support

- Chrome (Latest)
- Firefox (Latest)
- Safari (Latest)
- Edge (Latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🚀 Next Steps

### Phase 2: Implementation Tasks
1. **Populate All Classes**
   - Structure class7.json similarly
   - Structure class8.json similarly
   - Structure class9.json similarly
   - Structure class10.json similarly

2. **Add More Subjects**
   - English
   - Hindi
   - Social Studies
   - Computer Science

3. **Create Content Management UI**
   - Form-based JSON editor
   - Chapter/lesson builder
   - Resource uploader
   - Direct JSON preview

4. **Advanced Features**
   - Quiz and assessments
   - Certificates on completion
   - Student accounts & progress saving
   - Discussion forums
   - Downloadable course materials

## 🔗 Quick Links

- **Landing Page**: `index.html` (or `landing.html`)
- **View Math Course**: `class.html?class=6&subject=Mathematics&medium=English`
- **View Science Course**: `class.html?class=6&subject=Science&medium=Telugu`

## 💡 Tips for Customization

### Change Colors
Edit CSS variables in the `<style>` section:
```css
/* Change primary color from #a435f0 to your color */
```

### Add Subject Icons
Modify `getIconForSubject()` function in `landing.html`:
```javascript
const subjectMap = {
  'Mathematics': 'fa-calculator',
  'Your Subject': 'fa-your-icon'
};
```

### Update Course Metadata
Edit the `courseOverview` object in each JSON file.

## 🐛 Troubleshooting

### Content not loading?
1. Check browser console (F12) for errors
2. Verify JSON file path is correct
3. Check that class JSON file exists in `config/` folder

### Videos not playing?
1. Verify YouTube embed URLs
2. Check that URLs include `embed/` (not `/watch`)
3. Ensure videos are embeddable

### Medium selector not working?
1. Verify `chapterTitleTelugu` and `nameTelugu` fields exist in JSON
2. Check that `mediums` array includes "Telugu"

## 📞 Support

For issues or questions about the platform implementation, refer to the documentation above or contact the development team.

---

**Last Updated**: April 2026
**Version**: 1.0
**Platform Type**: Educational Course Platform
