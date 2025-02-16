from PyPDF2 import PdfReader
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("BROWSER_DRIVER_PATH")
cv = os.getenv("CV_PATH")

reader = PdfReader(cv)
number_of_pages = len(reader.pages)
text = ''.join([reader.pages[i].extract_text() for i in range(number_of_pages)])

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path=f"{path}",
    )
)

initial_actions = [
	{'open_tab': {'url': 'https://www.linkedin.com/feed/'}},
]

async def main():
    agent = Agent(
       task=(
           "Continuously search and apply for job postings on LinkedIn until stopped by the user. "
           "1. Go to LinkedIn and log in. "
           "2. Navigate to the ‘İş ilanları’ tab and search for ‘Software Developer’ positions in Istanbul. "
           "3. Scan the job postings and click on each listing to review its details. "
           "4. Extract the job summary and compare it with the CV content: {text}. "
           "5. If the job description matches the CV, proceed with the application; otherwise, skip to the next job. "
           "6. If the job is marked as ‘Kolay Başvuru’ and aligns with the CV, apply immediately. "
           "7. Select the appropriate salary expectation based on job seniority (e.g., Junior positions should have a lower salary range). "
           "8. Answer application questions automatically, including multiple-choice, short answers, and yes/no questions. "
           "9. Click ‘İleri’ at each step and finalize the application if a ‘Submit Application’ button appears. "
           "10. If an application requires an external website, skip it and move to the next listing. "
           "11. Repeat this process until the user provides a stop signal."
       ),
        llm=ChatOpenAI(model='gpt-4o'),
        browser=browser,
        initial_actions=initial_actions,
        save_conversation_path="logs/conversation"
    )

    result = await agent.run(max_steps=1000)
    input('Press Enter to close the browser...')
    await browser.close()
    print(result)
    
if __name__ == '__main__':
    asyncio.run(main())