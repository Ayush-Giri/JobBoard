from django.db import models
from django.contrib.auth import get_user_model
from locations.models import City, Country
from skills.models import Skills
from industry.models import Industry
from locations.models import City, Country

# Create your models here.

User = get_user_model()


class ApplicantProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="applicant_profile_image/", null=True, blank=True)
    headline = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    years_of_experience = models.SmallIntegerField(null=True, blank=True)
    current_job_title = models.CharField(max_length=200, null=True, blank=True)
    current_company = models.CharField(max_length=200, null=True, blank=True)
    expected_salary = models.IntegerField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.ManyToManyField(Skills, related_name="applicant_skills", null=True, blank=True)
    linkedin_url = models.URLField(max_length=250, null=True, blank=True)
    github_url = models.URLField(max_length=250, null=True, blank=True)
    portfolio_url = models.URLField(max_length=250, null=True, blank=True)
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)


    def __str__(self):
        return f"{self.user.username} | {self.user.email}"
    


# user OneToOneField → User
# company_name CharField
# company_logo ImageField, nullable (max 2MB)
# company_description TextField
# industry CharField
# company_size TextChoices: 1-10 / 11-50 / 51-200 / 200+
# founded_year PositiveIntegerField, nullable
# website_url URLField, nullable
# contact_person_name / contact_email / phone_number CharField / EmailField / CharField
# city / country / address CharField; address nullable
# linkedin_company_url URLField, nullable


class CompanySize(models.TextChoices):
    one_to_ten = ("1-10", "1-10")
    eleven_to_fifty = ("11-50", "11-50")
    fiftyone_to_twohundred = ("51-200", "51-200")

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_field = models.CharField(max_length=255, null=True, blank=True)
    company_logo = models.ImageField(upload_to="company_logo", null=True, blank=True)
    company_description = models.TextField(null=True, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    company_size = models.CharField(max_length=10, choices=CompanySize.choices, null=True, blank=True)
    website_url = models.URLField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    coutry = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    linked_in_company_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.role}"


    




    










# Employer Profile
# Company Info

# Company name
# Company logo
# Company description
# Industry (e.g. Healthcare, Tech, Finance)
# Company size (1-10 / 11-50 / 51-200 / 200+) — TextChoices
# Founded year
# Website URL

# Contact Info

# Contact person full name
# Contact email
# Phone number

# Location

# City
# Country
# Full address (optional)

# Social

# LinkedIn company page URL