from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_course_links(driver, url):
    driver.get(url)

    # Клік на кнопку для відкриття списку курсів
    courses_button = driver.find_element(By.XPATH, "//button[@data-qa='header-courses-dropdown-button']")
    courses_button.click()

    time.sleep(2)

    # Збір усіх посилань на курси
    courses = driver.find_elements(By.XPATH,
                                   "//a[@class='Button_transparentLight__T1185 Button_medium__XjfCa Button_fullWidth__EcevO DropdownProfessionsItem_link__4NmVV show-for-large Button_button__5Fngg']")

    course_links = []
    for course in courses:
        link = course.get_attribute('href')
        course_links.append(link)

    return course_links


def get_course_details(driver, course_url):
    driver.get(course_url)  # Перехід на сторінку курсу один раз

    course_details = {}

    try:
        # Отримання назви курсу
        title_element = driver.find_element(By.XPATH,
                                            "//h1[@class='typography_headingXHuge__0y2t9 CoursesHeadingText_heading__4tGVX hide-for-small-only']")
        course_details['title'] = title_element.text.strip().split(":")[0].strip()
    except:
        course_details['title'] = None

    try:
        # Отримання короткого опису курсу
        description_element = driver.find_element(By.XPATH,
                                                  "//p[@class='typography_textMain__oRJ69 CourseModulesList_aboutCourse__gmavO']")
        course_details['description'] = description_element.text.strip()
    except:
        course_details['description'] = None

    try:
        # Отримання типу курсу (повний день або у вільний час)
        full_day_button = driver.find_elements(By.XPATH, "//span[contains(text(), 'Навчатися повний день')]")
        free_time_button = driver.find_elements(By.XPATH, "//span[contains(text(), 'Навчатися у вільний час')]")
        if full_day_button and free_time_button:
            course_details['format'] = "full-time / flex"
        elif full_day_button:
            course_details['format'] = "only full-time"
        elif free_time_button:
            course_details['format'] = "only flex"
        else:
            course_details['format'] = "no group openings"
    except:
        course_details['format'] = None

    return course_details


if __name__ == "__main__":
    driver = webdriver.Chrome()

    url = "https://mate.academy"  # Замість цього ви можете використовувати ваш власний URL сторінки

    course_links = get_course_links(driver, url)

    for link in course_links:
        course_info = get_course_details(driver, link)

        print(f"Course name: {course_info['title']}.")
        print(f"Short description: {course_info['description']}")
        print(f"Course type: {course_info['format']}.\n")

    driver.quit()
