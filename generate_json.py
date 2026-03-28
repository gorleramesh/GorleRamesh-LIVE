import os
import json
import re
from bs4 import BeautifulSoup

def extract_youtube_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    iframes = soup.find_all('iframe', src=lambda x: x and 'youtube.com/embed' in x)
    return [iframe['src'] for iframe in iframes]

def extract_chapters_and_videos(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    chapters = []
    current_chapter = None
    for element in soup.find_all(['h4', 'iframe']):
        if element.name == 'h4' and 'logotext' in element.get('class', []):
            if current_chapter and current_chapter['videos']:
                chapters.append(current_chapter)
            current_chapter = {'topic': element.get_text().strip(), 'videos': []}
        elif element.name == 'iframe' and current_chapter:
            src = element.get('src')
            if src and 'youtube.com/embed' in src:
                current_chapter['videos'].append(src)
    if current_chapter and current_chapter['videos']:
        chapters.append(current_chapter)
    return chapters

def process_class(class_num):
    if class_num == 10:
        return process_class10()
    else:
        return process_lower_class(class_num)

def process_lower_class(class_num):
    main_file = f"{class_num}th Class.html" if class_num == 6 else f"{class_num}thClass.html"
    with open(main_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    subjects = []
    for one in soup.find_all('div', class_='one'):
        p = one.find('p')
        a = one.find('a', href=True)
        if p and a and a['href'].startswith(f'Chapter{class_num}') and a['href'].endswith('.html') and not a['href'].startswith(f'Chapter{class_num}PS'):
            subject_name = p.get_text().strip()
            subject_file = a['href']
            if os.path.exists(subject_file):
                with open(subject_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                chapters = extract_chapters_and_videos(content)
                chapterwisedetails = []
                priority = 1
                for chap in chapters:
                    if chap['videos']:
                        subtopics = [{'name': f'Video {j+1}', 'description': '', 'link': link} for j, link in enumerate(chap['videos'])]
                        chapterwisedetails.append({
                            'chapter': f'Chapter {priority}',
                            'topic': chap['topic'],
                            'priority': priority,
                            'subtopics': subtopics
                        })
                        priority += 1
                if chapterwisedetails:
                    subject_dict = {
                        'class': str(class_num),
                        'subject': subject_name,
                        'medium': 'English',
                        'chapterwisedetails': chapterwisedetails
                    }
                    # Add resources if PS file exists
                    ps_file = f'Chapter{class_num}PS EM.html'
                    if os.path.exists(ps_file):
                        subject_dict['resources'] = [{'name': 'Problem Set', 'link': ps_file}]
                    subjects.append(subject_dict)
    return subjects

def process_class10():
    main_file = '10thClass.html'
    with open(main_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    chapters_links = {}
    for a in soup.find_all('a', href=True):
        href = a['href']
        if 'Chapter10.' in href and href.endswith('.html'):
            text = a.get_text().strip()
            # extract chapter number or name
            match = re.search(r'(\d+)\.', href)
            if match:
                chap_num = int(match.group(1))
                key = chap_num
            else:
                key = href.replace('Chapter10. ', '').replace('.html', '').strip()
            chapters_links[key] = {'file': href, 'topic': text}
    
    subjects = {}
    for key, info in chapters_links.items():
        file = info['file']
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            soup_file = BeautifulSoup(content, 'html.parser')
            h4 = soup_file.find('h4', class_='logotext')
            topic = h4.get_text().strip() if h4 else info['topic']
            videos = extract_youtube_from_html(content)
            if videos:
                subtopics = [{'name': f'Video {j+1}', 'description': '', 'link': link} for j, link in enumerate(videos)]
                if isinstance(key, int):
                    if key <= 4:
                        subj = 'Chemistry'
                    else:
                        subj = 'Physics'
                else:
                    subj = 'Physics'  # for Atomic Structure, etc.
                if subj not in subjects:
                    subjects[subj] = []
                priority = key if isinstance(key, int) else len(subjects[subj]) + 1
                subjects[subj].append({
                    'chapter': f'Chapter {key}' if isinstance(key, int) else key,
                    'topic': topic,
                    'priority': priority,
                    'subtopics': subtopics
                })
    json_data = []
    for subj, chaps in subjects.items():
        json_data.append({
            'class': '10',
            'subject': subj,
            'medium': 'English',
            'chapterwisedetails': sorted(chaps, key=lambda x: x['priority'])
        })
    return json_data

# Process classes 6 to 10
for class_num in [6, 7, 8, 9, 10]:
    data = process_class(class_num)
    with open(f'config/class{class_num}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'Created config/class{class_num}.json')