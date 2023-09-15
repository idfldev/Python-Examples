from django.db import models
from django.contrib.auth.models import User


# Define a model for your roles, if needed
class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Define your IDFL Staffs model
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    # Add other fields related to employees

    def __str__(self):
        return self.user.username


# SECTION 1. APPLICANT INFORMATION =============================
class Companies(models.Model):
    company_name = models.CharField(max_length=255)
    company_name_english = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()


# SECTION 2. PAYMENT INFORMATION ===============================
class PayerCompanyInformation(models.Model):
    CURRENCY_CHOICES = [
        ("", ""),
        ("USD", "USD"),
        ("VND", "VND"),
        ("TWD", "TWD"),
        ("EURO", "EURO"),
        ("RMB", "RMB"),
        ("INR", "INR"),
        ("JPY", "JPY"),
        ("TRY", "TRY"),
        ("CHF", "CHF"),
        ("BDT", "BDT"),
        ("PKR", "PKR"),
        ("KHR", "KHR"),
    ]
    payment_currency = models.CharField(
        max_length=5,
        choices=CURRENCY_CHOICES,
        default="",
        blank=True,
    )
    another_currency_type = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=20)
    rush_3_days = models.BooleanField()
    rush_7_days = models.BooleanField()
    same_as_applicant = models.BooleanField()
    company_name = models.CharField(max_length=255)
    company_name_english = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()

# SECTION 4. PRODUCTS ===========================================
class ProductDetails(models.Model):
    description = models.CharField(max_length=255)

class ProductCategory(models.Model):
    product_name = models.CharField(max_length=255)
    product_details = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)


# SECTION 5. FACILITIES AND PROCESSES =============================
class FacilityAndProcessText(models.Model):
    facility = models.CharField(max_length=255)
    facility_unit_address = models.TextField()
    number_of_employees = models.IntegerField()
    list_of_activities_processes = models.TextField()
    certified_previously = models.BooleanField()

class FacilityAndProcess(models.Model):
    required = models.BooleanField()
    facilities_and_processes = models.ManyToManyField(FacilityAndProcessText)


# SECTION 3. STANDARDS =========================================
class Standard(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Standards(models.Model):
    STANDARDS_CHOICES = [
        ("ocs", "OCS"),
        ("gots", "GOTS"),
        ("grs", "GRS"),
        ("rcs", "RCS"),
        ("rds", "RDS"),
        ("raf", "RAF"),
        ("rws", "RWS"),
        ("rms", "RMS"),
        ("ras", "RAS"),
    ]
    standards_name = models.ManyToManyField("Standard", choices=STANDARDS_CHOICES, blank=True)

class CertificationStatus(models.Model):
    initial_certification = models.BooleanField()
    renewal_certification = models.BooleanField()
    previously_currently = models.CharField(max_length=255)
    license_no = models.CharField(max_length=255)
    certification_body = models.CharField(max_length=255)
    certification_expiration_date = models.DateField()

class Section3(models.Model):
    standard_name = models.ForeignKey(Standards, on_delete=models.CASCADE)
    section4 = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    section5 = models.ForeignKey(FacilityAndProcess, on_delete=models.CASCADE)


# ========= SECTION 6. CERTIFICATION INFORMATION ==========
class CertificationInformation(models.Model):
    oeko_tex_step = models.BooleanField()
    scs_recycled_content_verification = models.BooleanField()
    bsci_social_audit = models.BooleanField()
    sa8000_audit = models.BooleanField()
    fem = models.BooleanField()
    fslm = models.BooleanField()
    brm = models.BooleanField()
    wrap = models.BooleanField()
    gscp_social = models.BooleanField()
    gscp_environmental = models.BooleanField()
    facilities_of_gots = models.BooleanField()
    chemicals_of_gots = models.BooleanField()
    facilities_of_grs = models.BooleanField()
    chemicals_of_grs_products = models.BooleanField()
    certification_body = models.BooleanField()
    certification_body_text = models.TextField()
    product_certification_text = models.TextField()
    company_name = models.CharField(max_length=255)
    registered_seal_stamp = models.ImageField(upload_to="seal_stamps")
    authorized_signature = models.ImageField(upload_to="signatures")
    title_of_signatory = models.CharField(max_length=255)
    date_of_signature = models.DateField()
    application_representative = models.CharField(max_length=255)
    application_contact_name = models.CharField(max_length=255)
    representative_contact_email = models.EmailField()


class ApplicantInformation(models.Model):
    section1 = models.ForeignKey(Companies, on_delete=models.CASCADE)
    section2 = models.ForeignKey(PayerCompanyInformation, on_delete=models.CASCADE)
    section3 = models.ForeignKey(Section3, on_delete=models.CASCADE)
    section6 = models.ForeignKey(CertificationInformation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Applicant: {self.section1.company_name}, Payer: {self.section2.company_name}, Section 3: {self.section3.standard_name}, Section 6: {self.section6.title_of_signatory}"
