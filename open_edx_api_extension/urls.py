from django.conf.urls import url
from django.conf import settings

from open_edx_api_extension import views


urlpatterns = [
    url(r'^courses/$', views.CourseList.as_view()),
    url(r'^courses/proctored$', views.CourseListWithExams.as_view()),
    url(r'^enrollment$', views.SSOEnrollmentListView.as_view(), name='courseenrollments'),
    url(r'^user_proctored_exams/(?P<username>[\W\w]+)/$',
        views.ProctoredExamsListView.as_view(), name='user_proctored_exams'),
    url(r'^paid_mass_enrollment$', views.PaidMassEnrollment.as_view()),
    url(r'^update_verified_cohort$', views.UpdateVerifiedCohort.as_view()),
    url(r'^subscriptions$', views.Subscriptions.as_view()),
    url(r'^credentials$', views.Credentials.as_view()),
    url(r'^user_proctored_exam_attempt/(?P<attempt_code>[^/]*)/$', views.ProctoredExamsAttemptView.as_view()),
    url(r'^calendar/{}'.format(settings.COURSE_KEY_PATTERN), views.CourseCalendar.as_view(), name="course-calendar"),
    url(r'edx_proctoring/proctoring_poll_statuses_attempts/$', views.AttemptStatuses.as_view(),
        name='edx_proctoring.anonymous.proctoring_poll_statuses_attempts'),
    url(r'edx_proctoring/attempts_bulk_update/$', views.AttemptsBulkUpdate.as_view(),
        name='edx_proctoring.attempts_bulk_update'),
    url(r'^cohorts/cohort_names', views.CourseCohortNames.as_view()),
    url(r'^cohorts/cohorts_with_students', views.CourseCohortsWithStudents.as_view()),
    url(r'^course_structure$', views.CourseStructure.as_view()),
]
