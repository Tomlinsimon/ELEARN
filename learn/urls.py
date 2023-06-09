from django.urls import path
import learn.views


urlpatterns = [
    path('',learn.views.home,name='home'),
    path('home',learn.views.home,name='home'),
    path('news', learn.views.news, name='news'),
    path('about/',learn.views.about,name='about'),
    path('Contact',learn.views.contact,name='Contact'),
    path('login/',learn.views.login,name='login'),
    path('logout/',learn.views.logout,name='logout'),
    path('register_st',learn.views.register_st,name='register_st'),

    path('view', learn.views.view, name='view'),

    path('register_tr', learn.views.register_tr, name='register_tr'),

    path('admin_rg', learn.views.admin_rg, name='admin_rg'),
    path('admin_home', learn.views.admin_home, name='admin_home'),

    path('teacher_home', learn.views.teacher_home, name='teacher_home'),

    path('student_home', learn.views.student_home, name='student_home'),

    path('about_content',learn.views.abb,name='about_content'),

    path('add_blog',learn.views.add_blog,name='add_blog'),

    path('blogs_admin',learn.views.blogs_admin,name='blogs_admin'),

    path('blog_approves/<id>',learn.views.blog_approves,name='blog_approves'),

    path('blog_rejects/<id>',learn.views.blog_rejects,name='blog_rejects'),

    path('blog_delete/<id>', learn.views.blog_delete,name='blog_delete'),

    path('view_blog',learn.views.view_blog,name='view_blog'),

    path('update_pr_tr',learn.views.update_pr_tr,name='update_pr_tr'),

    path('guest',learn.views.g_m,name='guest'),

    path('delete_g_msg/<id>',learn.views.delete_g_msg,name='delete_g_msg'),

    path('update_pr_st',learn.views.update_pr_st,name='update_pr_st'),

    path('adm_prof',learn.views.adm_prof,name='adm_prof'),

    path('del_admin/<id>',learn.views.del_admin,name='del_admin'),

    path('edit_admin',learn.views.edit_admin,name='edit_admin'),

    path('subject_tr',learn.views.subject_tr,name='subject_tr'),

    path('edit_subject/<id>/<idd>/<idm>',learn.views.edit_subject,name='edit_subject'),

    path('delete_subject/<id>/<idd>/<idm>',learn.views.delete_subject,name='delete_subject'),

    path('add_subject',learn.views.add_subject,name='add_subject'),

    path('chapter_tr',learn.views.chapter_tr,name='chapter_tr'),


    path('edit_chapter/<id>/<idd>/<idk>/<idm>', learn.views.edit_chapter, name='edit_chapter'),


    path('delete_chapter/<id>/<idd>/<idk>/<idm>', learn.views.delete_chapter, name='delete_chapter'),


    path('add_chapter', learn.views.add_chapter, name='add_chapter'),


    path('add_chapter1', learn.views.add_chapter1, name='add_chapter1'),

    path('ch_co_tr',learn.views.ch_co_tr,name='ch_co_tr'),

    path('edit_content/<id>',learn.views.edit_content,name='edit_content'),

    path('delete_content/<id>',learn.views.delete_content,name='delete_content'),

    path('add_ch_con',learn.views.add_ch_con,name='add_ch_con'),

    path('add_chapter_c0',learn.views.add_chapter_c0,name='add_chapter_c0'),

    path('add_chapter_c1',learn.views.add_chapter_c1,name='add_chapter_c1'),

    path('stu_sub_selnew',learn.views.stu_sub_selnew,name='stu_sub_selnew'),

    path('st_sub_selnew2',learn.views.st_sub_selnew2,name='st_sub_selnew2'),

    path('disp_teach',learn.views.disp_teach,name='disp_teach'),

    path('stu_buk_teacherr/<id>',learn.views.stu_buk_teacherr,name='stu_buk_teacherr'),

    path('stu_buk_teacher',learn.views.stu_buk_teacher,name='stu_buk_teacher'),

    path('stu_buk_acc',learn.views.stu_buk_acc,name='stu_buk_acc'),

    path('stu_accept/<id>',learn.views.stu_accept,name='stu_accept'),

    path('stu_reject/<id>',learn.views.stu_reject,name='stu_reject'),

    path('stu_delete/<id>',learn.views.stu_delete,name='stu_delete'),

    path('st_book_courses',learn.views.st_book_courses,name='st_book_courses'),

    path('acc_chapter/<id>/<ikm>/<sub>',learn.views.acc_chapter,name='acc_chapter'),

    path('acc_chapter1',learn.views.acc_chapter1,name='acc_chapter1'),

    path('compp',learn.views.compp,name='compp'),

    path('st_pr',learn.views.st_pr,name='st_pr'),

    path('sched_test',learn.views.sched_test,name='sched_test'),

    path('sched_test1',learn.views.sched_test1,name='sched_test1'),

    path('sched_test3',learn.views.sched_test3,name='sched_test3'),

    path('ex_not',learn.views.ex_not,name='ex_not'),

    path('start_test', learn.views.start_test,name='start_test'),

    path('save_exam',learn.views.save_exam,name='save_exam'),

    path('exam_result1',learn.views.exam_result1,name='exam_result1'),

    path('exam_result',learn.views.exam_result,name='exam_result'),

    path('delete_ex_re/<id>',learn.views.delete_ex_re,name='delete_ex_re'),


    path('delete_test1/<id>', learn.views.delete_test1, name='delete_test1'),

    path('delete_test',learn.views.delete_test,name='delete_test'),

    path('upl_cer',learn.views.upl_cer,name='upl_cer'),

    path('do_cer',learn.views.do_cer,name='do_cer'),

    path('del_cer',learn.views.del_cer,name='del_cer'),

    path('delete_cert/<id>',learn.views.delete_cert,name='delete_cert'),

    path('subject_ad',learn.views.subject_ad,name='subject_ad'),

    path('edit_subject1/<id>/<idd>/<idt>/<pkm>',learn.views.edit_subject1,name='edit_subject1'),

    path('delete_subject1/<id>/<idd>/<idt>/<pkm>',learn.views.delete_subject1,name='delete_subject1'),

   path('chapter_ad',learn.views.chapter_ad,name='chapter_ad'),

    path('edit_chapter1/<id>/<idd>/<idt>/<idk>/<pkm>',learn.views.edit_chapter1,name='edit_chapter1'),

    path('delete_chapter1/<id>/<idd>/<idt>/<idk>',learn.views.delete_chapter1,name='delete_chapter1'),

    path('ch_co_ad',learn.views.ch_co_ad,name='ch_co_ad'),

    path('edit_content1/<id>',learn.views.edit_content1,name='edit_content1'),

    path('delete_content1/<id>',learn.views.delete_content1,name='delete_content1'),

    path('m_m2',learn.views.m_m2,name='m_m2'),

    path('del_msg_student/<id>',learn.views.del_msg_student,name='del_msg_student'),

    path('reply_msg_student/<id>',learn.views.reply_msg_student,name='reply_msg_student'),

    path('sent_msg_student',learn.views.sent_msg_student,name='sent_msg_student'),


    path('m_m1', learn.views.m_m1, name='m_m1'),


    path('del_msg_teacher/<id>', learn.views.del_msg_teacher, name='del_msg_teacher'),


    path('reply_msg_teacher/<id>', learn.views.reply_msg_teacher, name='reply_msg_teacher'),


    path('sent_msg_teacher', learn.views.sent_msg_teacher, name='sent_msg_teacher'),

    path('m_m', learn.views.m_m, name='m_m'),

    path('del_msg_admin/<id>', learn.views.del_msg_admin, name='del_msg_admin'),

    path('reply_msg_admin/<id>', learn.views.reply_msg_admin, name='reply_msg_admin'),

    path('sent_msg_admin', learn.views.sent_msg_admin, name='sent_msg_admin'),

    path('block',learn.views.block,name='block'),

    path('blocks/<id>',learn.views.blocks,name='blocks'),

    path('blocks1/<id>',learn.views.blocks1,name='blocks1'),

    path('allows/<id>',learn.views.allows,name='allows'),

    path('allows1/<id>',learn.views.allows1,name='allows1'),

    path('feedback',learn.views.feedback,name='feedback'),

    path('feedbak', learn.views.feedbak, name='feedbak'),

    path('delete_feedback/<id>',learn.views.delete_feedback,name='delete_feedback'),

    path('atten',learn.views.atten,name='atten'),
    ]