from django.shortcuts import render
# Create your views here.

posts = [
  {
    "author": "John Doe",
    "title": "The Importance of Sleep",
    "content": "Getting enough sleep is crucial for overall health and well-being. Lack of sleep can lead to a variety of health issues, including increased stress levels, impaired cognitive function, and a weakened immune system. It is recommended that adults get between 7-9 hours of sleep per night to ensure optimal health.",
    "date_posted": "2020-01-15"
  },
  {
    "author": "Jane Smith",
    "title": "The Benefits of Exercise",
    "content": "Regular exercise has numerous benefits for both the body and mind. It can help to improve cardiovascular health, increase muscle strength and flexibility, and boost mood and mental well-being. Aim for at least 150 minutes of moderate-intensity exercise per week for optimal results.",
    "date_posted": "2020-02-02"
  },
  {
    "author": "David Johnson",
    "title": "Eating Well on a Budget",
    "content": "Eating a nutritious diet doesn't have to break the bank. By planning meals, buying in bulk, and opting for affordable yet healthy ingredients, it is possible to eat well on a budget. Look for sales, use coupons, and consider growing your own fruits and vegetables to save even more.",
    "date_posted": "2020-03-20"
  },
  {
    "author": "Sarah Wilson",
    "title": "The Power of Positive Thinking",
    "content": "Positive thinking can have a profound impact on our lives. By focusing on the good, practicing gratitude, and reframing negative thoughts, we can improve our mental and emotional well-being. Surround yourself with positive people and engage in activities that bring you joy.",
    "date_posted": "2020-04-12"
  },
  {
    "author": "Michael Brown",
    "title": "Stress Management Techniques",
    "content": "Stress is a normal part of life, but it is important to find healthy ways to manage it. Some effective stress management techniques include exercise, deep breathing, meditation, and spending time in nature. Find what works best for you and make self-care a priority.",
    "date_posted": "2020-05-05"
  },
  {
    "author": "Emily Davis",
    "title": "The Art of Time Management",
    "content": "Effective time management is key to being productive and achieving your goals. Prioritize tasks, eliminate distractions, and break larger tasks into smaller, more manageable ones. Use tools like calendars and to-do lists to stay organized and make the most of your time.",
    "date_posted": "2020-06-18"
  },
  {
    "author": "Robert Wilson",
    "title": "The Importance of Setting Goals",
    "content": "Setting goals gives us direction and motivation in life. Whether they are short-term or long-term, having goals helps us to focus and work towards something meaningful. Make sure your goals are specific, measurable, achievable, relevant, and time-bound for the best results.",
    "date_posted": "2020-07-09"
  },
  {
    "author": "Jennifer Lee",
    "title": "Building Healthy Relationships",
    "content": "Healthy relationships are built on trust, communication, and mutual respect. It is important to listen actively, express your needs and boundaries, and resolve conflicts in a constructive manner. Surround yourself with people who uplift and support you.",
    "date_posted": "2020-08-27"
  },
  {
    "author": "Christopher Green",
    "title": "The Benefits of Mindfulness",
    "content": "Mindfulness is the practice of being fully present in the moment and non-judgmentally aware of your thoughts and feelings. It can help to reduce stress, improve focus and concentration, and enhance overall well-being. Incorporate mindfulness into your daily routine through meditation, deep breathing, or simply taking a few moments to pause and be present.",
    "date_posted": "2020-09-14"
  },
  {
    "author": "Amanda Taylor",
    "title": "The Importance of Self-Care",
    "content": "Self-care is essential for maintaining good physical, mental, and emotional health. It involves taking time to prioritize your own needs and engage in activities that bring you joy and relaxation. Practice self-care regularly to prevent burnout and improve overall well-being.",
    "date_posted": "2020-10-30"
  }
]

def home(request):
    context ={
        'posts':posts,
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')