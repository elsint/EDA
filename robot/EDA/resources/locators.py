eda_lex_locators = {
    "app_launcher": {
        "app_link": "//div[contains(@class, 'slds-section slds-is-open')]//section[@id='cards']//a[@class='appTileTitle' and text()='{}']",
    },
    "placeholder_lookup": {
        "lookup1": "//div[@class='slds-lookup__result-text' and contains(text(), '{}')]",
        "lookup2": "//mark[text() = '{}']/ancestor::a",
    },
    "input": {
        "input1": "//label[text()='{}']/following::input",
        "input2": "//input[@type='text' and @data-name='{}']"
    },
    "listbox": {
        "title": "//label[contains(text(), '{}')]/following::input[contains(@class, 'slds-input slds-combobox__input') and @role='textbox']",
        "value": "//*[contains(@class, 'slds-listbox__option') and @data-value='{}']",
    },
    "frame": "//iframe[contains(@id, '{}') or contains(@title, '{}') or contains(@name, '{}')]",
    "input_placeholder": "//input[contains(@placeholder,'{}')]",
    "navigation_menu": "//button[@title='Show Navigation Menu']",
    "contacts_tab": "//a[@title='{}']",
    "navigation_tab": "//button[@title='Show Navigation Menu']/../descendant::a[@title='{}']",
    "tab_menu": "//a[@title='{}']",
    "choose_tab": " //a[text()='{}']",
    "tab_tab": "//a[@title='Contacts']/../descendant::a[@title='{}']",
    "toast_message": "//span[contains(@class, 'toastMessage') and text()='{}']",
    "success_message": "//div[@id='successToast']//h2[text()='{}']",
    "toast_close": "//div[contains(@class, 'slds-theme--success')]/button[contains(@class, 'slds-notify__close')]",
    "close_tab": "//*[@data-key='close']/ancestor::button[contains(@class, 'slds-button slds-button_icon-x-small')]",
    "mailing_address": "//*[contains(@placeholder,'{}')]",
    "object_dd": "//h1[contains(@class,'slds-page-header__title')]/a/div[contains(@class,'triggerLinkTextAndIconWrapper')][.//lightning-primitive-icon]",
    "record": {
        "actions": "//div[contains(@class, 'actionsContainer')]/descendant::a[@title='{}']",
        "tab_header": "//div[@role='tablist']/descendant::a[contains(@class, 'tabHeader') and @title='{}']",
        "button": "//div[@class='actionsContainer']/button[@title='{}']",
        "datepicker": "//div[contains(@class,'uiDatePickerGrid')]/table[@class='calGrid']//span[text()='{}']",
        "edit_button": '//*[@title="{}"]',
        "list_old": "//div[contains(@class,'forcePageBlockSectionRow')]/div[contains(@class,'forcePageBlockItem')]/div[contains(@class,'slds-p-vertical_xx-small')]/div[@class='slds-form-element__control']/div[.//span[text()='{}']][//div[contains(@class,'uiMenu')]//a[@class='select']]",
        "list": "//div[contains(@class,'forcePageBlockItem')]//div//div//div//span//span[contains(text(), 'Primary Address Type')]/../../div/div/div/div/a[@class='select']",
        "dropdown": "//div[@class='select-options']/ul[@class='scrollable']/li[@class='uiMenuItem uiRadioMenuItem']/a[contains(text(),'{}')]",
        "related": {
            "new": "//div[@class='container']/descendant::div[contains(@class, 'slds-card__header')]/header/descendant::span[text()='{}']/ancestor::header/following-sibling::div/descendant::a[@title='New']",
            "button": "//article[contains(@class, 'forceRelatedListCardDesktop')][.//img][.//span[@title='{}']]//a[@title='{}']",
            "check_occurence": '//h2/a/span[@title="{}"]/following-sibling::span[text()=" ({})"]',
            "drop-down": '//div[contains(@class, "slds-card")]/header[.//span[@title="{}"]]/parent::*/div/div/div/a[contains(@class, "slds-button")]',
            "title": '//div[contains(@class, "slds-card")]/header[.//span[@title="{}"]]',
        },
    },
    "object": {
        "radio_button": "//div[contains(@class,'changeRecordTypeRightColumn')]/div/label[@class='slds-radio']/div[.//span[text()='{}']]/preceding::div[1]/span[@class='slds-radio--faux']",
        "contact_role": '//tbody//a[text()= "{}"]/../../following-sibling::td/span/span[text() = "{}"]',
        "record": '//tbody//a[text()= "{}"]',
    },
    
    "eda_settings": {
        "tab": "//div[@id='tabs']/descendant::li[contains(@class, 'slds-text-heading--label')]/a[text()='{}']",
        "edit": "//button[contains(@class, 'slds-button') and @type='button']/span[text()='Edit']/..",
        "checkbox_default": "//span[text()='{}']/../following-sibling::div/descendant::img",
        "checkbox": "//span[text()='{}']/../following-sibling::div/descendant::label[contains(@class,'slds-checkbox')]/span[contains(@class, 'slds-checkbox--faux')]",
        "save": "//div[contains(@class, 'slds-page-header')]/descendant::button[contains(@class, 'settings-save-bttn')]",
        "system_tab": "//a[contains(text(),'System')]",
        "affiliations_tab": "//a[contains(text(),'Affiliations')]",
        "affiliations_check": "//span[text()='Specify Role for Created Affiliations:']/../following-sibling::div/div/div/label/span/img[@class = 'copy-start-date checked' and @alt='True']",
        "affiliations_role_checkbox": "//input[@class='copy-start-date uiInput uiInputCheckbox uiInput--default uiInput--checkbox']/following-sibling::span",
        "affiliations_role_checkbox1": "(//label[@class='slds-checkbox']//span[@class='uiImage uiOutputCheckbox'])[3]//img",
        "affiliation_mappings_tab": "//a[contains(text(), 'Affiliation Mappings')]",
        "create_walkin_advising_event_button": "//div[@id='main']//button[contains(text(), 'New Walk-In')]",
        "courses": "//a[contains(text(),'Courses')]",
        "duration": "//div[.//span[text()='Duration'] and contains(@class, 'slds-form-element') ]//select//option[@value='60']",
        "hh_naming_check": "//input[@class='automatic-hh-acc uiInput uiInputCheckbox uiInput--default uiInput--checkbox']/following-sibling::span",
        "hh_naming_role_checkbox": "//select[@class='admin-account-naming-input-select select uiInput uiInputSelect uiInput--default uiInput--select']//option[@value='{{!{{!FirstName}}}} {{!LastName}} Administrative Account']",
        "hh_adminfnamelname": "//input[contains(@class,'firstName')]",
        "course_connections_tab": "//a[contains(text(),'Course Connections')]",
        "cc_checkbox": "//input[contains(@class,'slds-checkbox')]/parent::label",
        "student_select": "//select[contains(@class,'student-course-connection-record-type-input-select')]",
        "faculty_select": "//select[contains(@class,'faculty-course-connection-record-type-input-select')]",
    },
    "tabs": {
        "accountsandcontacts" : "//a[contains(text(),'Accounts and Contacts')]",
    },
    "account_types": {
        "administrative": "//span[contains(text(),'Administrative')]/parent::*",
        "academic": "//div[contains(@class,'slds-form-element__control')]//span[contains(text(),'Academic Program')]",
        "administrativecheckbox": "//div[contains(@class,'slds-form-element__control')]//span[contains(text(),'Administrative')]",
        "business": "//div[contains(@class,'slds-form-element__control')]//span[contains(text(),'Business Organization')]",
        "educational": "//div[contains(@class,'slds-form-element__control')]//span[contains(text(),'Educational Institution')]",
        "household": "//div[contains(@class,'slds-form-element__control')]//span[contains(text(),'Household Account')]",
        "sports": "//div[contains(@class,'slds-form-element__control')]//span[contains(text(),'Sports Organization')]",
        "university": "//div[contains(@class,'slds-form-element__control')]//span[contains(text(),'University Department')]",
        "save": "//button[contains(@class, 'slds-button')]/span[text()='Save']/..",
        "edit": "//button[contains(@class, 'slds-button')]/span[text()='Edit']/..",
        "cancel": "//button[contains(@class, 'slds-button')]/span[text()='Cancel']/..",
    },
    "contact": {
        "new_button": "//a[@title='New']//div[@title='New']",
        "first_name": "//input[contains(@class,'firstName')]",
        "last_name":  "//input[contains(@class,'lastName')]",
        "save_button": "//button[@title='Save']",
        "oldprogram_enrollment_new_button": "//div[@class='container forceRelatedListSingleContainer']/following::span[@title='Program Enrollments']/following::a//div[@title='New']",
        "program_enrollment_new_button": "//div[contains(@class, 'windowViewMode-normal')]//span[text()='Program Enrollments']/following-sibling::span[@title='(0)']/ancestor::header/following-sibling::div/descendant::a[@title='New']",
    },
    "program_plans": {
        "program_plan": "(//a[@title='Program Plans'])[2]/span/span",
        "program_plan1": "//a[@title='Program Plans']//span[@class='label-ctr slds-app-launcher__tile-body slds-app-launcher__tile-body--small']//span[contains(text(), 'Program Plans')]",
        "main_drop": "(//div//one-app-nav-bar-item-root//a//span[contains(text(), 'Program Plans')]//..)[1]",
        "new_button": "//a[@title='New']//div[@title='New']/..",
        "pp_name": "//div//div//div//div//div//div//div//label//span[contains(text(), 'Program Plan Name')]//../following-sibling::input",
        "save_button": "//div[contains(@class, 'inlineFooter')]/descendant::button[@title='Save']",
    },
    "plan_requirement": {
        "error": "//div[contains(@class, 'pageLevelErrors')]/descendant::li[text()='{}']",
        "parent_plan_req_name": "//div[contains(@class, 'slds-modal__container')]/descendant::span[text()='Parent Plan Requirement']/../following-sibling::div/descendant::span[text()='{}']",
        "plan_requirement_name": "//div[contains(@class, 'slds-modal__container')]/descendant::span[text()='Plan Requirement Name']/../following-sibling::input",
        "program_plan_name": "//td/a[@title='{}']",
        "program_plan": "//div[contains(@class, 'slds-modal__container')]/descendant::span[text()='Program Plan']/../following-sibling::div/descendant::span[text()='{}']",
        "delete_field": "//div[contains(@class, 'slds-modal__container')]/descendant::span[text()='{}']/../following-sibling::div/descendant::span[text()='{}']/following-sibling::a[@class='deleteAction']",
        "toast_message": "//lightning-icon[contains(@class, 'toastIcon') and contains(@class, 'slds-icon-utility-success')]",
    },
    "course_offering": {
        "main_tab": "//a[@title='Course Offerings']//span[@class='label-ctr slds-app-launcher__tile-body slds-app-launcher__tile-body--small']//span[contains(text(), 'Course Offerings')]",
        "search_courses": "//div/input[@title='Search Courses']",
        "new_button": "//a[@title='New']//div[@title='New']/..",
        "new_course_button": "//span[@class='itemLabel slds-truncate slds-show--inline-block slds-m-left--xx-small' and contains(text(), 'New Course')]",
        "save_button": "(//span[@class=' label bBody' and text()='Save']/ancestor::button[contains(@class, 'slds-button')])[3]",
        "next_save_button_old": "//button[@class='slds-button slds-button--neutral uiButton--default uiButton--brand uiButton forceActionButton']//span[@class=' label bBody' and contains(text(), 'Save')]",
        "next_save_button": "//div[contains(@class, 'inlineFooter')]/descendant::button[@title='Save']",
        "final_save_button": "(//span[@class=' label bBody' and text()='Save'])[3]/ancestor::button",
    },
    "term": {
        "new_term_button": "//span[@class='itemLabel slds-truncate slds-show--inline-block slds-m-left--xx-small' and contains(text(), 'New Term')]//..",
        "save_button": "(//span[@class=' label bBody' and contains(text(), 'Save')])[5]/..",
        "account": "//div//input[@title='Search Accounts']",
        "search_terms": "//input[@title='Search Terms']",
        "course_offering_id": "//span[contains(text(), 'Course Offering ID')]//../following-sibling::input",
    },
    "eda_tile": "//div[@class='slds-app-launcher__tile-body']//a[contains(text(),'EDA')]/../..",
    "new_account": "//span[@title='New Account']",
    "new_account_next_button": "//button[contains(@class, 'slds-button')]//span[@class=' label bBody' and text()='Next']",
    "new_account_name": "//input[@class='input uiInput uiInputText uiInput--default uiInput--input']",
    "new_account_save_button": "//div[contains(@class, 'slds-modal__footer')]/descendant::button[@title='Save']",
    "academic_program": "//span[contains(text(), 'Academic Program')]",
    "new_program_enrollment_save_button": "//div[contains(@class, 'inlineFooter')]/descendant::button[@title='Save']",
    "affiliated_accounts_count": "//span[text()='Affiliated Accounts']/following-sibling::span[contains(@title, '(1)')]",
    "program_enrollments_count": "//span[text()='Program Enrollments']/following-sibling::span[contains(@title, '(1)')]",
    "programenrollment_account": "//div[@class='autocompleteWrapper slds-grow']//input[@class=' default input uiInput uiInputTextForAutocomplete uiInput--default uiInput--input uiInput uiAutocomplete uiInput--default uiInput--lookup']",
    "list_of_departments": "//button[contains(@class, 'slds-button slds-button--neutral')]//span[@class=' label bBody' and text()='Next']",
    "tab": "//div[@class='uiTabBar']/ul[@class='tabs__nav']/li[contains(@class,'uiTabItem')]/a[@class='tabHeader']/span[contains(text(), '{}')]",
    "desktop_rendered": "css: div.desktop.container.oneOne.oneAppLayoutHost[data-aura-rendered-by]",
    "loading_box": "css: div.auraLoadingBox.oneLoadingBox",
    "spinner": "css: div.slds-spinner",
    "affiliations_tab": "//a[contains(text(),'Affiliations')]",
    "locating_delete_dropdown": '//tbody//a[text()= "{}"]/../../following-sibling::td/span//div/a/lightning-icon',
    "related_name": '//tbody/tr/td/a[contains(@class,"forceOutputLookup")]',
    "rel_loc_dd": "//tbody/tr[{}]/td[4]//lightning-primitive-icon",
    "delete_icon": '//span[contains(text() ,"{}")]/following::span[. = "{}"]/following-sibling::a/child::span[@class = "deleteIcon"]',
    "aff_list": '//div[@role="tablist"]/following::div[@class = "container forceRelatedListSingleContainer"][7]/article/div[@class="slds-card__body"]/div/div/div/div/div/div/div/table/tbody/tr/td[1]',
    "aff_status": '//table[contains(@class,"forceRecordLayout")]/tbody/tr[.//th/div/a[contains(@class,"textUnderline")]][.//td/a[@title="{}"]]/td[3]',
    "aff_id": '//table[contains(@class,"forceRecordLayout")]/tbody/tr[.//th/div/a[contains(@class,"textUnderline")]][.//td/a[@title="{}"]]/th//a',
    "click_aff_id": '//table[contains(@class,"forceRecordLayout")]/tbody/tr/th/div/a[text()="{}"]',
    "check_status": '//div[contains(@class, "forcePageBlockItem")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]/span[.//span[text()="{}"]]',
    "check_field": '//div[contains(@class, "forcePageBlockItem")][.//span[text()="{}"]]//following-sibling::div[.//span[contains(@class, "test-id__field-value")]]/span/div//a[text()="{}"]',
    "account_list": '//tbody/tr/th[.//span[contains(@class, "slds-grid")]]/descendant::a[text()="{}"]',
    "dd_options": '//*[@id="p3"]/option[text()="{}"]',
    "related_list_items": '//div[@class = "forceRelatedListContainer"][.//a[contains(@class, "slds-card")]]//span[text() = "{}"]/ancestor::div[contains(@class, "slds-card")]/following-sibling::div[contains(@class, "slds-card")][.//div[contains(@class, "outputLookupContainer")]]//a[text()="{}"]',
    "header_field_value": '//li[contains(@class,"slds-page-header__detail")]//div//span[contains(@title,"{}")]/following-sibling::div/div/div/a[contains(text(), "{}")]',
    "header_datepicker": '//li[contains(@class, "slds-page-header__detail")][.//p[contains(@class, "slds-text-heading--label")][@title="{}"]]//*[@class="uiOutputDate"]',
    "affiliated_contacts": '//div[@class = "forceRelatedListContainer"][.//a[contains(@class, "slds-card")]]//span[text() = "{}"]/ancestor::div[contains(@class, "slds-card")]/following-sibling::div[contains(@class, "slds-card")]//tbody//td/span[text()="{}"]/../following-sibling::td/span[text()="{}"]',
    "detail_page": {
        "address": '//h3[contains(@class, "slds-section__title")][.//span[contains(text(),"Address")]]/../..//div[contains(@class, "test-id")]/span[text()= "{}"]/../following-sibling::div//a[@title = "{}"]/div[contains(@class, "slds")]',
        "field": '//h3[contains(@class, "slds-section__title")][.//span[text()="{}"]]/../..//div[contains(@class, "test-id")]/span[text()= "{}"]/../following-sibling::div//span[text()="{}"]',
        "verify_field_value": '//div[contains(@class, "forcePageBlockItem")]/div/div//span[text()="{}"]/../../div[2]/span/span[text() = "{}"]',
    },
    "manage_hh_page": {
        "address": '//div[contains(@class, "uiInput")][.//label[contains(@class, "uiLabel")]/span[text()="{}"]]/',
        "mhh_checkbox": '//*[@id="SortCanvas"]/li//a[text()="{}"]/ancestor::div[contains(@class, "slds-card__header")]/following-sibling::div[contains(@class,"slds-card__body")]//form//div//label/span[@id = "{}"]',
        "button": '//*[contains(@title, "{}")]',
        "mhh_button": '//span[text()="{}"]',
    },
    "modal": {
        "checkbox": '//div[contains(@class,"uiInputCheckbox")]/label/span[text()="{}"]/../following-sibling::input[@type="checkbox"]',
        "save": "//div[contains(@class, 'footer') or contains(@class, 'Footer')]/descendant::button[@title='Save']",
    },
    "opportunity": {
        "contact_role": '//div[contains(@class,"listItemBody")][./h3//a[text()="{}"]]//parent::h3/following-sibling::ul/li/div[contains(@class,"forceListRecordItem")]/div[@title="Role:"]/following-sibling::div/span[text()="{}"]',
    },
    "input_placeholder": "//input[contains(@placeholder,'{}')]",
    "package": {
        "name": "//table[@class='list']/tbody/tr[{}]/th/a",
        "version": "//table[@class='list']/tbody/tr[{}]/td[4]",
    },    
}

contacts_locators = {
    "action_shortcut": "//div[contains(@class, 'slds-utility-panel')]/descendant::button[@type='button' and text()='{}']",
    "contact_save": "//div[contains(@class,'modal-footer')]//button[@title='Save']//span[text()='Save']",
    "header": "//a[@title='Contacts']//span",
    "select_contact": "//a[@title='{} {}']",
    "edit_contact": "//div[contains(@class,'windowViewMode-normal')]/descendant::div//a[@title='Edit']//div[@title='Edit']",
    "preferred_phone": "//span//span[contains(text(),'Preferred Phone')]",
    "preferred_phone_home_dropdown": "//span//span[contains(text(),'Preferred Phone')]/following::span/following::a",
    "preferred_tab": "//div[@class='select-options']/descendant::a[@title='Home']",
    "home_phone": "//input[@type='tel']/preceding-sibling::label/span[contains(text(),'Home Phone')]",
    "phone_verify_has_number": "(//div//span[text()='Phone']/../following-sibling::div//span[not( text()='123-123-1234')])[1]",
    "preferred_error_message": "//li[contains(text(), 'The phone selected for Preferred Phone can')]",
    "which_preferred_error_message": "//li[contains(text(), 'Tell us which Phone is preferred.')]",
    "field_for_home_phone": "//div//label//span[contains(text(),'Home Phone')]/../following-sibling::input",
    "field_for_work_phone": "//div//label//span[contains(text(),'Work Phone')]/../following-sibling::input",
    "field_for_phone": "//div//label//span[text()='Phone']/../following-sibling::input",
    "footer_cancel": "//div[contains(@class,'modal-footer')]//span[text()='Cancel']",
    "which_footer_cancel": "//div[contains(@class,'footer')]/button[@title='Cancel']//span[text()='Cancel']",
    "footer_save": "//div[contains(@class,'modal-footer')]//span[text()='Save']",
    "toast_message": "//span[contains(@class, 'toastMessage') and contains(text(),'{}')]",
    "disable_preferred_phone": "//div/span[text()='Disable Preferred Phone enforcement:']/following::div[1]/div/div/label/span/img[@alt='False']",
    "preferred_phone_active": "//div/span[text()='Disable Preferred Phone enforcement:']/following::div[1]/div/div/label/span/img[@alt='True']",
    "disable_checked": "(//span[text()='Disable Preferred Phone enforcement:']/following::div/div/div/label/input/following-sibling::span)[1]",
    "accounts_contacts": "//a[contains(text(),'Accounts and Contacts')]",
    "tab_menu": "//a[@title='{}']",
    "tab_tab": "//a[@title='Contacts']/../descendant::a[@title='{}']",
    "details_tab": "//div[contains(@class,'normal')]//span[@class='title' and text()='Details']",
    "phone_home": "//span[text()='Home Phone']/../following-sibling::input",
    "run_cleanup": "//button[text()='Run Cleanup']",
    "phone_field": "//div//span[text()='Phone']/../following-sibling::div//span//span[text()='123-123-1234']",
    "phone_verify": "//div//span[text()='Phone']/../following-sibling::div//span//span[text()='123-123-1234']",
    "home_phone_verify": "//span[text()='Home Phone']/../following::div//span//span[text()='123-123-1234']",
    "copy_from": "//select[@class='contact-preferred-phone-picklist-input-select select uiInput uiInputSelect uiInput--default uiInput--select']",
    "copy_from_home_phone": "//select[@class='contact-preferred-phone-picklist-input-select select uiInput uiInputSelect uiInput--default uiInput--select']//option[@value='Home Phone']",
    "successful_run": "//span[text()='The process was queued successfully. An email will be sent at the completion of the job.']",
    "enhanced_preferred_clear": "//div/span[text()='Enable Enhanced Preferred Phone Functionality:']/following::div[1]/div/div/label/span/img[@alt='False']",
    "enhanced_preferred_clear_faux": "//span[text()='Enable Enhanced Preferred Phone Functionality:']/following::div[1]/div/div/label/input/following::span[1]",
    "enhanced_preferred_set": "//span[text()='Enable Enhanced Preferred Phone Functionality:']/following::div[1]/div/div/label/span/img[@alt='True']",
    "enhanced_preferred_set_faux": "//span[text()='Enable Enhanced Preferred Phone Functionality:']/following::div[1]/div/div/label/input/following::span[1]",

}
