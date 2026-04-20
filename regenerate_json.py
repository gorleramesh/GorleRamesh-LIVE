#!/usr/bin/env python3
import os
import json
import re
from bs4 import BeautifulSoup
from pathlib import Path

def extract_youtube_links_from_html(html_content):
    """Extract YouTube embed links from HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    iframes = soup.find_all('iframe', src=lambda x: x and 'youtube.com/embed' in x)
    return [iframe['src'] for iframe in iframes]

def extract_chapters_from_html(html_content):
    """
    Extract chapters and their videos from HTML.
    Returns a list of dicts with 'chapter_name' and 'videos' keys.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    chapters = []
    
    # Find all h4 elements with class 'logotext'
    h4_elements = soup.find_all('h4', class_='logotext')
    
    for i, h4 in enumerate(h4_elements):
        chapter_name = h4.get_text().strip()
        
        # Find all iframes that come after this h4 until the next h4
        videos = []
        current = h4.find_next()
        
        # Determine where this chapter ends (at next h4 or end of document)
        next_h4 = h4.find_next('h4', class_='logotext')
        
        while current:
            # Stop if we've reached the next h4
            if current == next_h4:
                break
            
            # Check if this is an iframe with YouTube embed
            if current.name == 'iframe' and 'youtube.com/embed' in current.get('src', ''):
                videos.append(current['src'])
            
            current = current.find_next()
        
        if videos:
            chapters.append({
                'chapter_name': chapter_name,
                'videos': videos
            })
    
    return chapters

def process_class_6_7(class_num):
    """Process classes 6 and 7 which have separate Math and Science files."""
    subjects_data = []
    
    # Determine file pattern
    if class_num == 6:
        chapter_pattern = "Chapter6"
        math_file = "Chapter6Mat EM.html"
        science_file = "Chapter6Sci EM.html"
        ps_file = "Chapter6PS EM.html"
    else:
        chapter_pattern = "Chapter7"
        math_file = "Chapter7Mat EM.html"
        science_file = "Chapter7Sci EM.html"
        ps_file = "Chapter7PS EM.html"
    
    # Process Mathematics
    if os.path.exists(math_file):
        with open(math_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chapters = extract_chapters_from_html(content)
        if chapters:
            chapter_details = []
            for chap in chapters:
                subtopics = [
                    {
                        "name": f"Video {i+1}",
                        "description": "",
                        "link": link,
                        "type": "video"
                    }
                    for i, link in enumerate(chap['videos'])
                ]
                
                chapter_details.append({
                    "chapter": chap['chapter_name'],
                    "subtopics": subtopics,
                    "resources": [
                        {
                            "name": "Problem Set",
                            "link": ps_file,
                            "type": "html"
                        }
                    ]
                })
            
            subjects_data.append({
                "class": str(class_num),
                "subject": "Mathematics",
                "medium": "English",
                "chapterwisedetails": chapter_details
            })
    
    # Process Science
    if os.path.exists(science_file):
        with open(science_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chapters = extract_chapters_from_html(content)
        if chapters:
            chapter_details = []
            for chap in chapters:
                subtopics = [
                    {
                        "name": f"Video {i+1}",
                        "description": "",
                        "link": link,
                        "type": "video"
                    }
                    for i, link in enumerate(chap['videos'])
                ]
                
                chapter_details.append({
                    "chapter": chap['chapter_name'],
                    "subtopics": subtopics,
                    "resources": [
                        {
                            "name": "Problem Set",
                            "link": "Chapter{}PS EM.html".format(class_num),
                            "type": "html"
                        }
                    ]
                })
            
            subjects_data.append({
                "class": str(class_num),
                "subject": "Science",
                "medium": "English",
                "chapterwisedetails": chapter_details
            })
    
    return subjects_data

def process_class_8_9(class_num):
    """Process classes 8 and 9 which have individual chapter files."""
    subjects_data = []
    
    chapter_pattern = f"Chapter{class_num}"
    
    # Find all chapter files for this class
    chapter_files = {}
    for file in sorted(os.listdir('.')):
        # Match files like "Chapter8. 1. Force and Pressure.html"
        if file.startswith(chapter_pattern) and file.endswith('.html') and 'PS' not in file and 'Lesson' not in file:
            # Extract chapter number
            match = re.search(r'Chapter\d+\.\s*(\d+)', file)
            if match:
                chapter_num = int(match.group(1))
                
                # Extract chapter name from file
                chapter_name = file.replace(f'{chapter_pattern}. ', '').replace('.html', '')
                
                chapter_files[chapter_num] = {
                    'file': file,
                    'name': chapter_name
                }
    
    # Process each chapter file
    chapters_data = []
    for chapter_num in sorted(chapter_files.keys()):
        file_info = chapter_files[chapter_num]
        file_path = file_info['file']
        chapter_name = file_info['name']
        
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            videos = extract_youtube_links_from_html(content)
            
            subtopics = [
                {
                    "name": f"Video {i+1}",
                    "description": "",
                    "link": link,
                    "type": "video"
                }
                for i, link in enumerate(videos)
            ]
            
            chapters_data.append({
                "chapter": chapter_name,
                "subtopics": subtopics,
                "resources": [
                    {
                        "name": "Problem Set NCERT",
                        "link": f"{chapter_pattern}PS NCERT.html",
                        "type": "html"
                    },
                    {
                        "name": "Problem Set EM",
                        "link": f"{chapter_pattern}PS EM.html",
                        "type": "html"
                    },
                    {
                        "name": "Problem Set TM",
                        "link": f"{chapter_pattern}PS TM.html",
                        "type": "html"
                    }
                ]
            })
    
    if chapters_data:
        subjects_data.append({
            "class": str(class_num),
            "subject": "Science",
            "medium": "English",
            "chapterwisedetails": chapters_data
        })
    
    return subjects_data

# Create config directory if it doesn't exist
os.makedirs('config', exist_ok=True)

# Process classes 6-9
print("Regenerating JSON files for classes 6-9...")
print()

for class_num in [6, 7]:
    print(f"Processing class {class_num}...")
    data = process_class_6_7(class_num)
    with open(f'config/class{class_num}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Created config/class{class_num}.json")
    for subject in data:
        num_chapters = len(subject['chapterwisedetails'])
        print(f"    - {subject['subject']}: {num_chapters} chapter(s)")
    print()

for class_num in [8, 9]:
    print(f"Processing class {class_num}...")
    data = process_class_8_9(class_num)
    with open(f'config/class{class_num}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Created config/class{class_num}.json")
    for subject in data:
        num_chapters = len(subject['chapterwisedetails'])
        print(f"    - {subject['subject']}: {num_chapters} chapter(s)")
    print()

print("Done! All JSON files have been regenerated.")
