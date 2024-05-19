# NSBE_InclusiviTea

## Inspiration
4.8%. This is the population of African Americans in Canada. In a place as culturally diverse, there is a lack of inclusive spaces for minorities. We want to make a platform where cultures can share their experiences of places in our city to promote or discourage certain meeting spaces.

## What it does
1. Safety and Inclusivity: Users, especially from minority communities, often face challenges in finding spaces where they feel safe, welcome, and represented. This application provides a curated list of places that are ou publicly reviewed by the community.
2. Community Empowerment: By highlighting businesses and locations that actively support inclusivity, the app empowers minority communities to support businesses that align with their values.
3. Cultural Representation: The application helps in locating spaces where cultural representation is evident, thus encouraging the celebration and understanding of diverse heritages within Canadian cities.

## How it was built
The project starts with the OSM database (similar to Google Maps), and getting information about potential meeting spaces like their names and addresses. We take that data and organize it into a database of meeting spaces. Each meeting space is then given a rating for each minority group that we support on our platform (currently African American, Indigenous, and LGBTQ). A javascript server is implemented to allow users to interact with the platform, find meeting spaces and leave their rating of that place for a specific culture. Cohere AI was intended to be used to filter out toxic/spam reviews that malicious users might leave. Pytorch was intended to be used to caption images that would be passed into it from an 'image getter' that we also wrote in Python.

## Challenges Faced
Porting the integration of Cohere AI from Python to Javascript for our review feature.  
Adapting our platform to be compatible with multiple languages posed difficulties (ie. a python web crawler that we wanted to use).  
Tackling our first hackathon proved challenging due to the lack of previous experience.  
Learning new topics as we delved into new technologies and concepts.  
Consistent debugging efforts across various components of the project due to lack of experience.  

## Accomplishments to Celebrate
Successfully resolving and debugging issues throughout the project.  
Overcoming the hurdles and challenges encountered during development.  
Embracing the learning opportunities and expanding our skill sets.  
Building meaningful connections and friendships within the hackathon community.  

## Lessons Learned
Gaining proficiency in new programming languages.  
Familiarizing ourselves with different frameworks and tools.  
Learning about AI technologies, including PyTorch and Cohere.  
Participation in insightful workshops to broaden our knowledge.  
Honing debugging skills through hands-on problem-solving.  

## Future Plans for InclusiviTea
Conducting in-depth research and development for continual improvement.  
Customizing the platform to align with user needs and preferences.  
Enhancing the overall user experience through innovative features.  
Ensuring scalability to accommodate potential growth and increased usage.  
