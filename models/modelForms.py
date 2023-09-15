from django.db import models

class ApplicantInformation(models.Model):
    company_name = models.CharField(max_length=255)
    company_name_english = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()

class PayerCompanyInformation(models.Model):
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

class Section2(models.Model):
    payment_currency = models.CharField(max_length=255)
    another_currency_type = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=20)
    payer_company_information = models.ForeignKey(PayerCompanyInformation, on_delete=models.CASCADE)

class Section3(models.Model):
    ocs = models.BooleanField()
    gots = models.BooleanField()
    grs = models.BooleanField()
    rcs = models.BooleanField()
    rds = models.BooleanField()
    raf = models.BooleanField()
    rws = models.BooleanField()
    rms = models.BooleanField()
    ras = models.BooleanField()

class CertificationStatus(models.Model):
    initial_certification = models.BooleanField()
    renewal_certification = models.BooleanField()
    previously_currently = models.CharField(max_length=255)
    license_no = models.CharField(max_length=255)
    certification_body = models.CharField(max_length=255)
    certification_expiration_date = models.DateField()

class ProductCategory(models.Model):
    home_textiles_bedding = models.CharField(max_length=255)
    apparel = models.CharField(max_length=255)
    accessories = models.CharField(max_length=255)
    footwear = models.CharField(max_length=255)
    fabrics = models.CharField(max_length=255)
    yarns = models.CharField(max_length=255)
    fibers = models.CharField(max_length=255)
    filling_stuffing = models.CharField(max_length=255)
    packaging = models.CharField(max_length=255)
    recycled_materials = models.CharField(max_length=255)
    other_product = models.CharField(max_length=255)
    required = models.BooleanField()

class FacilityAndProcess(models.Model):
    facility = models.CharField(max_length=255)
    facility_unit_address = models.TextField()
    number_of_employees = models.IntegerField()
    list_of_activities_processes = models.TextField()
    certified_previously = models.BooleanField()

class Section4(models.Model):
    facilities_and_processes = models.ManyToManyField(FacilityAndProcess)

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

class ChemicalCompliance(models.Model):
    facilities_of_gots = models.BooleanField()
    chemicals_of_gots = models.BooleanField()
    facilities_of_grs = models.BooleanField()
    chemicals_of_grs_products = models.BooleanField()

class CertificationCompliance(models.Model):
    certification_body = models.BooleanField()
    certification_body_text = models.CharField(max_length=255)
    product_certification = models.BooleanField()
    product_certification_text = models.CharField(max_length=255)

class ConfirmationInformation(models.Model):
    company_name = models.CharField(max_length=255)
    registered_seal_stamp1 = models.ImageField(upload_to='seal_stamps')
    registered_seal_stamp2 = models.ImageField(upload_to='seal_stamps')
    authorized_signature = models.ImageField(upload_to='signatures')
    title_of_signatory = models.CharField(max_length=255)
    date_of_signature = models.DateField()
    application_representative = models.CharField(max_length=255)
    application_contact_name = models.CharField(max_length=255)
    representative_contact_email = models.EmailField()
