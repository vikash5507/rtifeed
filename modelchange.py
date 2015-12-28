from rtiapp import models

sds = models.State_department.objects.all()
for sd in sds:
	sd.department.state = sd.state
	sd.department.save()
	print sd
print "OKOKOKOKOKOK"