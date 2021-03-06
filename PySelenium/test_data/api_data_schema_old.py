{
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "RequestSource",
    "Provider"
  ],
  "properties": {
    "RequestSource": {
      "$id": "#/properties/RequestSource",
      "type": "string",
      "title": "The Requestsource Schema",
      "default": "",
      "examples": [
        "API"
      ],
      "pattern": "^(.*)$"
    },
    "Provider": {
      "$id": "#/properties/Provider",
      "type": "object",
      "title": "The Provider Schema",
      "required": [
        "ProviderDemographics",
        "ProviderAlias",
        "ProviderSpeciality",
        "ProviderLicense",
        "ProviderLicenseStatusLog",
        "ProviderProfessionalLiability",
        "ProviderAppointmentAssociation",
        "ProviderCertification",
        "ProviderCMECredit",
        "ProviderCoveringCollaborating",
        "ProviderEducationTraining",
        "ProviderHealth",
        "ProviderHospitalPrivelege",
        "ProviderLanguages",
        "ProviderMalPractice",
        "ProviderOtherIdType",
        "ProviderReference",
        "ProviderEmploymentHistory",
        "Practice",
        "PracticeLocation",
        "ProviderPracticeLocation",
        "ProviderContractLine",
        "ProviderStatus"
      ],
      "properties": {
        "ProviderDemographics": {
          "$id": "#/properties/Provider/properties/ProviderDemographics",
          "type": "object",
          "title": "The Providerdemographics Schema",
          "required": [
            "ProviderCategory",
            "Gender",
            "NPI",
            "IsDummyNPI",
            "FirstName",
            "LastName",
            "Email"
          ],
          "properties": {
            "ProviderCategory": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/ProviderCategory",
              "type": "string",
              "title": "The Providercategory Schema",
              "default": "",
              "examples": [
                "Individual"
              ],
              "pattern": "^(.*)$"
            },
            "ProviderType": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/ProviderType",
              "type": "string",
              "title": "The Providertype Schema",
              "default": "",
              "examples": [
                "Dental"
              ],
              "pattern": "^(.*)$"
            },
            "DegreeTitle": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/DegreeTitle",
              "type": "string",
              "title": "The Degreetitle Schema",
              "default": "",
              "examples": [
                "MD"
              ],
              "pattern": "^(.*)$"
            },
            "Gender": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/Gender",
              "type": "string",
              "title": "The Gender Schema",
              "default": "",
              "examples": [
                "Male"
              ],
              "pattern": "^(.*)$"
            },
            "NPI": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/NPI",
              "type": "string",
              "title": "The Npi Schema",
              "default": "",
              "examples": [
                "1154665107"
              ],
              "pattern": "^(.*)$"
            },
            "IsDummyNPI": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/IsDummyNPI",
              "type": "string",
              "title": "The Isdummynpi Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "SSN": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/SSN",
              "type": "string",
              "title": "The Ssn Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "FirstName": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/FirstName",
              "type": "string",
              "title": "The Firstname Schema",
              "default": "",
              "maxLength": 20,
              "examples": [
                "Manish"
              ],
              "pattern": "^(.*)$"
            },
            "MiddleName": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/MiddleName",
              "type": "string",
              "title": "The Middlename Schema",
              "default": "",
              "examples": [
                "S"
              ],
              "pattern": "^(.*)$"
            },
            "LastName": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/LastName",
              "type": "string",
              "title": "The Lastname Schema",
              "default": "",
              "examples": [
                "Bisht"
              ],
              "pattern": "^(.*)$"
            },
            "PreferedName": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/PreferedName",
              "type": "string",
              "title": "The Preferedname Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "MaidenName": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/MaidenName",
              "type": "string",
              "title": "The Maidenname Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "SpouseName": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/SpouseName",
              "type": "string",
              "title": "The Spousename Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "Prefix": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/Prefix",
              "type": "string",
              "title": "The Prefix Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "Suffix": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/Suffix",
              "type": "string",
              "title": "The Suffix Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "CellPhone": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/CellPhone",
              "type": "string",
              "title": "The Cellphone Schema",
              "default": "",
              "examples": [
                "9829529565"
              ],
              "pattern": "^(.*)$"
            },
            "BirthDate": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/BirthDate",
              "type": "string",
              "title": "The Birthdate Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "Email": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/Email",
              "type": "string",
              "title": "The Email Schema",
              "default": "",
              "examples": [
                "msb.net.in@gmail.com"
              ],
              "pattern": "^(.*)$"
            },
            "Phone": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/Phone",
              "type": "string",
              "title": "The Phone Schema",
              "default": "",
              "examples": [
                "9829529565"
              ],
              "pattern": "^(.*)$"
            },
            "BirthCountry": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/BirthCountry",
              "type": "string",
              "title": "The Birthcountry Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "BirthState": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/BirthState",
              "type": "string",
              "title": "The Birthstate Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "BirthCity": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/BirthCity",
              "type": "string",
              "title": "The Birthcity Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "Ethinicity": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/Ethinicity",
              "type": "string",
              "title": "The Ethinicity Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "CountryOfCitizenShip": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/CountryOfCitizenShip",
              "type": "string",
              "title": "The Countryofcitizenship Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "Married": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/Married",
              "type": "string",
              "title": "The Married Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "OrganisationName": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/OrganisationName",
              "type": "string",
              "title": "The Organisationname Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "IsOwnerInvestor": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/IsOwnerInvestor",
              "type": "string",
              "title": "The Isownerinvestor Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "RelationshipToOrganisation": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/RelationshipToOrganisation",
              "type": "string",
              "title": "The Relationshiptoorganisation Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "HowToInformPatients": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/HowToInformPatients",
              "type": "string",
              "title": "The Howtoinformpatients Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            },
            "DbaOwner": {
              "$id": "#/properties/Provider/properties/ProviderDemographics/properties/DbaOwner",
              "type": "string",
              "title": "The Dbaowner Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            }
          }
        },
        "ProviderAlias": {
          "$id": "#/properties/Provider/properties/ProviderAlias",
          "type": "array",
          "title": "The Provideralias Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderAlias/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "Source",
              "FirstName",
              "MiddleName",
              "LastName"
            ],
            "properties": {
              "Source": {
                "$id": "#/properties/Provider/properties/ProviderAlias/items/properties/Source",
                "type": "string",
                "title": "The Source Schema",
                "default": "",
                "examples": [
                  "I-Network"
                ],
                "pattern": "^(.*)$"
              },
              "FirstName": {
                "$id": "#/properties/Provider/properties/ProviderAlias/items/properties/FirstName",
                "type": "string",
                "title": "The Firstname Schema",
                "default": "",
                "examples": [
                  "Mani"
                ],
                "pattern": "^(.*)$"
              },
              "MiddleName": {
                "$id": "#/properties/Provider/properties/ProviderAlias/items/properties/MiddleName",
                "type": "string",
                "title": "The Middlename Schema",
                "default": "",
                "examples": [
                  "S"
                ],
                "pattern": "^(.*)$"
              },
              "LastName": {
                "$id": "#/properties/Provider/properties/ProviderAlias/items/properties/LastName",
                "type": "string",
                "title": "The Lastname Schema",
                "default": "",
                "examples": [
                  "Bisht"
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderSpeciality": {
          "$id": "#/properties/Provider/properties/ProviderSpeciality",
          "type": "array",
          "title": "The Providerspeciality Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderSpeciality/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "SpecialityLevelName",
              "TaxonomyCode",
              "BoardStatus",
              "CertificationNumber",
              "CertificationDate",
              "ReCertificationDate",
              "ExpirationDate",
              "IsPursuing",
              "ExamDate",
              "Explanation",
              "BoardName",
              "BoardNPI",
              "MainWebsite",
              "BoardVerificationWebsite",
              "Address1",
              "Address2",
              "City"
            ],
            "properties": {
              "SpecialityLevelName": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/SpecialityLevelName",
                "type": "string",
                "title": "The Specialitylevelname Schema",
                "default": "",
                "examples": [
                  "Primary"
                ],
                "pattern": "^(.*)$"
              },
              "TaxonomyCode": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/TaxonomyCode",
                "type": "string",
                "title": "The Taxonomycode Schema",
                "default": "",
                "examples": [
                  "1223D0004X"
                ],
                "pattern": "^(.*)$"
              },
              "BoardStatus": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/BoardStatus",
                "type": "string",
                "title": "The Boardstatus Schema",
                "default": "",
                "examples": [
                  "Certified"
                ],
                "pattern": "^(.*)$"
              },
              "CertificationNumber": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/CertificationNumber",
                "type": "string",
                "title": "The Certificationnumber Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CertificationDate": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/CertificationDate",
                "type": "string",
                "title": "The Certificationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ReCertificationDate": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/ReCertificationDate",
                "type": "string",
                "title": "The Recertificationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ExpirationDate": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/ExpirationDate",
                "type": "string",
                "title": "The Expirationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsPursuing": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/IsPursuing",
                "type": "string",
                "title": "The Ispursuing Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ExamDate": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/ExamDate",
                "type": "string",
                "title": "The Examdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Explanation": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Explanation",
                "type": "string",
                "title": "The Explanation Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "BoardName": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/BoardName",
                "type": "string",
                "title": "The Boardname Schema",
                "default": "",
                "examples": [
                  "SC Board Test Peeyush"
                ],
                "pattern": "^(.*)$"
              },
              "BoardNPI": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/BoardNPI",
                "type": "string",
                "title": "The Boardnpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MainWebsite": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/MainWebsite",
                "type": "string",
                "title": "The Mainwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "BoardVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/BoardVerificationWebsite",
                "type": "string",
                "title": "The Boardverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressState": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/AddressState",
                "type": "string",
                "title": "The Addressstate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressCountry": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/AddressCountry",
                "type": "string",
                "title": "The Addresscountry Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EMail": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/EMail",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comments": {
                "$id": "#/properties/Provider/properties/ProviderSpeciality/items/properties/Comments",
                "type": "string",
                "title": "The Comments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderLicense": {
          "$id": "#/properties/Provider/properties/ProviderLicense",
          "type": "array",
          "title": "The Providerlicense Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderLicense/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "LicenseTypeName",
              "LicenseNumber",
              "IssueDate",
              "ExpirationDate",
              "State",
              "Country",
              "LicenseStatus",
              "BoardName",
              "BoardNPI",
              "MainWebsite",
              "BoardVerificationWebsite",
              "SysAdminComment",
              "TerminatedDate",
              "Address1",
              "Address2",
              "City",
              "AddressState",
              "Zip",
              "County",
              "AddressCountry",
              "Latitutde",
              "Longitude",
              "EMail",
              "Phone1",
              "Phone2",
              "Fax",
              "Comments"
            ],
            "properties": {
              "LicenseTypeName": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/LicenseTypeName",
                "type": "string",
                "title": "The Licensetypename Schema",
                "default": "",
                "examples": [
                  "DEA"
                ],
                "pattern": "^(.*)$"
              },
              "LicenseNumber": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/LicenseNumber",
                "type": "string",
                "title": "The Licensenumber Schema",
                "default": "",
                "examples": [
                  "12345"
                ],
                "pattern": "^(.*)$"
              },
              "IssueDate": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/IssueDate",
                "type": "string",
                "title": "The Issuedate Schema",
                "default": "",
                "examples": [
                  "01/01/2018"
                ],
                "pattern": "^(.*)$"
              },
              "ExpirationDate": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/ExpirationDate",
                "type": "string",
                "title": "The Expirationdate Schema",
                "default": "",
                "examples": [
                  "12/31/2019"
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  "CA"
                ],
                "pattern": "^(.*)$"
              },
              "Country": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Country",
                "type": "string",
                "title": "The Country Schema",
                "default": "",
                "examples": [
                  "USA"
                ],
                "pattern": "^(.*)$"
              },
              "LicenseStatus": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/LicenseStatus",
                "type": "string",
                "title": "The Licensestatus Schema",
                "default": "",
                "examples": [
                  "ACTIVE"
                ],
                "pattern": "^(.*)$"
              },
              "BoardName": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/BoardName",
                "type": "string",
                "title": "The Boardname Schema",
                "default": "",
                "examples": [
                  "American Board Electrodiagnostic Med"
                ],
                "pattern": "^(.*)$"
              },
              "BoardNPI": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/BoardNPI",
                "type": "string",
                "title": "The Boardnpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MainWebsite": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/MainWebsite",
                "type": "string",
                "title": "The Mainwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "BoardVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/BoardVerificationWebsite",
                "type": "string",
                "title": "The Boardverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SysAdminComment": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/SysAdminComment",
                "type": "string",
                "title": "The Sysadmincomment Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminatedDate": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/TerminatedDate",
                "type": "string",
                "title": "The Terminateddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressState": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/AddressState",
                "type": "string",
                "title": "The Addressstate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressCountry": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/AddressCountry",
                "type": "string",
                "title": "The Addresscountry Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EMail": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/EMail",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comments": {
                "$id": "#/properties/Provider/properties/ProviderLicense/items/properties/Comments",
                "type": "string",
                "title": "The Comments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderLicenseStatusLog": {
          "$id": "#/properties/Provider/properties/ProviderLicenseStatusLog",
          "type": "array",
          "title": "The Providerlicensestatuslog Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderLicenseStatusLog/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "LicenseNumber",
              "Status",
              "StartDate",
              "EndDate",
              "TerminationReason"
            ],
            "properties": {
              "LicenseNumber": {
                "$id": "#/properties/Provider/properties/ProviderLicenseStatusLog/items/properties/LicenseNumber",
                "type": "string",
                "title": "The Licensenumber Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Status": {
                "$id": "#/properties/Provider/properties/ProviderLicenseStatusLog/items/properties/Status",
                "type": "string",
                "title": "The Status Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "StartDate": {
                "$id": "#/properties/Provider/properties/ProviderLicenseStatusLog/items/properties/StartDate",
                "type": "string",
                "title": "The Startdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EndDate": {
                "$id": "#/properties/Provider/properties/ProviderLicenseStatusLog/items/properties/EndDate",
                "type": "string",
                "title": "The Enddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderLicenseStatusLog/items/properties/TerminationReason",
                "type": "string",
                "title": "The Terminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderProfessionalLiability": {
          "$id": "#/properties/Provider/properties/ProviderProfessionalLiability",
          "type": "array",
          "title": "The Providerprofessionalliability Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "PolicyType",
              "PolicyNumber",
              "Occurance",
              "Aggregate",
              "CoverageFrom",
              "CoverageTo",
              "RetroactiveDate",
              "ChangeReason",
              "TailCoverage",
              "Exclusions",
              "DeniedExplanation",
              "PrimaryInsuranceCarrierName",
              "PrimaryInsuranceNPI",
              "PrimaryMainWebsite",
              "PrimaryVerificationWebsite",
              "PrimaryComments",
              "PrimaryTerminatedDate",
              "PrimaryTerminationReason",
              "PrimaryAddress1",
              "PrimaryAddress2",
              "PrimaryCity",
              "PrimaryState",
              "PrimaryZip",
              "PrimaryCounty",
              "PrimaryCountry",
              "PrimaryLatitutde",
              "PrimaryLongitude",
              "PrimaryEMail",
              "PrimaryPhone1",
              "PrimaryPhone2",
              "PrimaryFax",
              "SecondryInsuranceCarrierName",
              "SecondryInsuranceNPI",
              "SecondryMainWebsite",
              "SecondryVerificationWebsite",
              "SecondryComments",
              "SecondryTerminatedDate",
              "SecondryTerminationReason",
              "SecondryAddress1",
              "SecondryAddress2",
              "SecondryCity",
              "SecondryState",
              "SecondryZip",
              "SecondryCounty",
              "SecondryCountry",
              "SecondryLatitutde",
              "SecondryLongitude",
              "SecondryEMail",
              "SecondryPhone1",
              "SecondryPhone2",
              "SecondryFax"
            ],
            "properties": {
              "PolicyType": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PolicyType",
                "type": "string",
                "title": "The Policytype Schema",
                "default": "",
                "examples": [
                  "Individual"
                ],
                "pattern": "^(.*)$"
              },
              "PolicyNumber": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PolicyNumber",
                "type": "string",
                "title": "The Policynumber Schema",
                "default": "",
                "examples": [
                  "21345"
                ],
                "pattern": "^(.*)$"
              },
              "Occurance": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/Occurance",
                "type": "string",
                "title": "The Occurance Schema",
                "default": "",
                "examples": [
                  "10"
                ],
                "pattern": "^(.*)$"
              },
              "Aggregate": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/Aggregate",
                "type": "string",
                "title": "The Aggregate Schema",
                "default": "",
                "examples": [
                  "10000"
                ],
                "pattern": "^(.*)$"
              },
              "CoverageFrom": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/CoverageFrom",
                "type": "string",
                "title": "The Coveragefrom Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CoverageTo": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/CoverageTo",
                "type": "string",
                "title": "The Coverageto Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "RetroactiveDate": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/RetroactiveDate",
                "type": "string",
                "title": "The Retroactivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ChangeReason": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/ChangeReason",
                "type": "string",
                "title": "The Changereason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TailCoverage": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/TailCoverage",
                "type": "string",
                "title": "The Tailcoverage Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Exclusions": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/Exclusions",
                "type": "string",
                "title": "The Exclusions Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DeniedExplanation": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/DeniedExplanation",
                "type": "string",
                "title": "The Deniedexplanation Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryInsuranceCarrierName": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryInsuranceCarrierName",
                "type": "string",
                "title": "The Primaryinsurancecarriername Schema",
                "default": "",
                "examples": [
                  "Insurance Career api"
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryInsuranceNPI": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryInsuranceNPI",
                "type": "string",
                "title": "The Primaryinsurancenpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryMainWebsite": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryMainWebsite",
                "type": "string",
                "title": "The Primarymainwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryVerificationWebsite",
                "type": "string",
                "title": "The Primaryverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryComments": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryComments",
                "type": "string",
                "title": "The Primarycomments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryTerminatedDate": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryTerminatedDate",
                "type": "string",
                "title": "The Primaryterminateddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryTerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryTerminationReason",
                "type": "string",
                "title": "The Primaryterminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryAddress1": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryAddress1",
                "type": "string",
                "title": "The Primaryaddress1 Schema",
                "default": "",
                "examples": [
                  "New Vihar"
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryAddress2": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryAddress2",
                "type": "string",
                "title": "The Primaryaddress2 Schema",
                "default": "",
                "examples": [
                  "Rajsthan"
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryCity": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryCity",
                "type": "string",
                "title": "The Primarycity Schema",
                "default": "",
                "examples": [
                  "ayars"
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryState": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryState",
                "type": "string",
                "title": "The Primarystate Schema",
                "default": "",
                "examples": [
                  "New York"
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryZip": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryZip",
                "type": "string",
                "title": "The Primaryzip Schema",
                "default": "",
                "examples": [
                  "85324"
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryCounty": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryCounty",
                "type": "string",
                "title": "The Primarycounty Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryCountry": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryCountry",
                "type": "string",
                "title": "The Primarycountry Schema",
                "default": "",
                "examples": [
                  "USA"
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryLatitutde": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryLatitutde",
                "type": "string",
                "title": "The Primarylatitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryLongitude": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryLongitude",
                "type": "string",
                "title": "The Primarylongitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryEMail": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryEMail",
                "type": "string",
                "title": "The Primaryemail Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryPhone1": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryPhone1",
                "type": "string",
                "title": "The Primaryphone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryPhone2": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryPhone2",
                "type": "string",
                "title": "The Primaryphone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryFax": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/PrimaryFax",
                "type": "string",
                "title": "The Primaryfax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryInsuranceCarrierName": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryInsuranceCarrierName",
                "type": "string",
                "title": "The Secondryinsurancecarriername Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryInsuranceNPI": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryInsuranceNPI",
                "type": "string",
                "title": "The Secondryinsurancenpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryMainWebsite": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryMainWebsite",
                "type": "string",
                "title": "The Secondrymainwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryVerificationWebsite",
                "type": "string",
                "title": "The Secondryverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryComments": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryComments",
                "type": "string",
                "title": "The Secondrycomments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryTerminatedDate": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryTerminatedDate",
                "type": "string",
                "title": "The Secondryterminateddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryTerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryTerminationReason",
                "type": "string",
                "title": "The Secondryterminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryAddress1": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryAddress1",
                "type": "string",
                "title": "The Secondryaddress1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryAddress2": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryAddress2",
                "type": "string",
                "title": "The Secondryaddress2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryCity": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryCity",
                "type": "string",
                "title": "The Secondrycity Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryState": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryState",
                "type": "string",
                "title": "The Secondrystate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryZip": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryZip",
                "type": "string",
                "title": "The Secondryzip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryCounty": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryCounty",
                "type": "string",
                "title": "The Secondrycounty Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryCountry": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryCountry",
                "type": "string",
                "title": "The Secondrycountry Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryLatitutde": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryLatitutde",
                "type": "string",
                "title": "The Secondrylatitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryLongitude": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryLongitude",
                "type": "string",
                "title": "The Secondrylongitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryEMail": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryEMail",
                "type": "string",
                "title": "The Secondryemail Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryPhone1": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryPhone1",
                "type": "string",
                "title": "The Secondryphone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryPhone2": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryPhone2",
                "type": "string",
                "title": "The Secondryphone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SecondryFax": {
                "$id": "#/properties/Provider/properties/ProviderProfessionalLiability/items/properties/SecondryFax",
                "type": "string",
                "title": "The Secondryfax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderAppointmentAssociation": {
          "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation",
          "type": "array",
          "title": "The Providerappointmentassociation Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "Association",
              "AppointmentDepartment",
              "FacultyRank",
              "AcademicTitle",
              "AppointmentStartDate",
              "AppointmentEndDate",
              "AssociationJoinedDate",
              "AssociationTerminationDate",
              "InstitutionName",
              "TerminationReason",
              "TerminationDate",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "County",
              "CountryName",
              "Latitutde",
              "Longitude",
              "AddressWebsite",
              "AddressVerificationWebsite",
              "EMail",
              "Phone1",
              "Phone2",
              "Fax",
              "AddressNPI",
              "AddressComments"
            ],
            "properties": {
              "Association": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Association",
                "type": "string",
                "title": "The Association Schema",
                "default": "",
                "examples": [
                  "MHSNJ"
                ],
                "pattern": "^(.*)$"
              },
              "AppointmentDepartment": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AppointmentDepartment",
                "type": "string",
                "title": "The Appointmentdepartment Schema",
                "default": "",
                "examples": [
                  "Oral Surgery"
                ],
                "pattern": "^(.*)$"
              },
              "FacultyRank": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/FacultyRank",
                "type": "string",
                "title": "The Facultyrank Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AcademicTitle": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AcademicTitle",
                "type": "string",
                "title": "The Academictitle Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AppointmentStartDate": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AppointmentStartDate",
                "type": "string",
                "title": "The Appointmentstartdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AppointmentEndDate": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AppointmentEndDate",
                "type": "string",
                "title": "The Appointmentenddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AssociationJoinedDate": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AssociationJoinedDate",
                "type": "string",
                "title": "The Associationjoineddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AssociationTerminationDate": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AssociationTerminationDate",
                "type": "string",
                "title": "The Associationterminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "InstitutionName": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/InstitutionName",
                "type": "string",
                "title": "The Institutionname Schema",
                "default": "",
                "examples": [
                  "ITTTns-12 - USANew York - Address 2 - West Virginia - 22225 -  - 3534543534 - 6598753164 - "
                ],
                "pattern": "^(.*)$"
              },
              "TerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/TerminationReason",
                "type": "string",
                "title": "The Terminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationDate": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/TerminationDate",
                "type": "string",
                "title": "The Terminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CountryName": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/CountryName",
                "type": "string",
                "title": "The Countryname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressWebsite": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AddressWebsite",
                "type": "string",
                "title": "The Addresswebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AddressVerificationWebsite",
                "type": "string",
                "title": "The Addressverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EMail": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/EMail",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressNPI": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AddressNPI",
                "type": "string",
                "title": "The Addressnpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressComments": {
                "$id": "#/properties/Provider/properties/ProviderAppointmentAssociation/items/properties/AddressComments",
                "type": "string",
                "title": "The Addresscomments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderCertification": {
          "$id": "#/properties/Provider/properties/ProviderCertification",
          "type": "array",
          "title": "The Providercertification Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderCertification/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "CertificationTypeName",
              "CertificationNo",
              "CertificationDate",
              "ExpirationDate",
              "ReCertificationDate",
              "IsPursuning",
              "ExamDate",
              "Explanation",
              "BoardName",
              "BoardNPI",
              "MainWebsite",
              "BoardVerificationWebsite",
              "TerminatedDate",
              "Address1",
              "Address2",
              "City",
              "AddressState",
              "Zip",
              "County",
              "AddressCountry",
              "Latitutde",
              "Longitude",
              "EMail",
              "Phone1",
              "Phone2",
              "Fax",
              "Comments"
            ],
            "properties": {
              "CertificationTypeName": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/CertificationTypeName",
                "type": "string",
                "title": "The Certificationtypename Schema",
                "default": "",
                "examples": [
                  "AB of Physical Therapy Specialties"
                ],
                "pattern": "^(.*)$"
              },
              "CertificationNo": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/CertificationNo",
                "type": "string",
                "title": "The Certificationno Schema",
                "default": "",
                "examples": [
                  "98484"
                ],
                "pattern": "^(.*)$"
              },
              "CertificationDate": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/CertificationDate",
                "type": "string",
                "title": "The Certificationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ExpirationDate": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/ExpirationDate",
                "type": "string",
                "title": "The Expirationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ReCertificationDate": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/ReCertificationDate",
                "type": "string",
                "title": "The Recertificationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsPursuning": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/IsPursuning",
                "type": "string",
                "title": "The Ispursuning Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ExamDate": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/ExamDate",
                "type": "string",
                "title": "The Examdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Explanation": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Explanation",
                "type": "string",
                "title": "The Explanation Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "BoardName": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/BoardName",
                "type": "string",
                "title": "The Boardname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "BoardNPI": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/BoardNPI",
                "type": "string",
                "title": "The Boardnpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MainWebsite": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/MainWebsite",
                "type": "string",
                "title": "The Mainwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "BoardVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/BoardVerificationWebsite",
                "type": "string",
                "title": "The Boardverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminatedDate": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/TerminatedDate",
                "type": "string",
                "title": "The Terminateddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressState": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/AddressState",
                "type": "string",
                "title": "The Addressstate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressCountry": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/AddressCountry",
                "type": "string",
                "title": "The Addresscountry Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EMail": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/EMail",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comments": {
                "$id": "#/properties/Provider/properties/ProviderCertification/items/properties/Comments",
                "type": "string",
                "title": "The Comments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderCMECredit": {
          "$id": "#/properties/Provider/properties/ProviderCMECredit",
          "type": "array",
          "title": "The Providercmecredit Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderCMECredit/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "CMECreditCategoryName",
              "CMECredits",
              "Title",
              "LocationName",
              "StartDate",
              "EndDate"
            ],
            "properties": {
              "CMECreditCategoryName": {
                "$id": "#/properties/Provider/properties/ProviderCMECredit/items/properties/CMECreditCategoryName",
                "type": "string",
                "title": "The Cmecreditcategoryname Schema",
                "default": "",
                "examples": [
                  "Category 1"
                ],
                "pattern": "^(.*)$"
              },
              "CMECredits": {
                "$id": "#/properties/Provider/properties/ProviderCMECredit/items/properties/CMECredits",
                "type": "string",
                "title": "The Cmecredits Schema",
                "default": "",
                "examples": [
                  "25"
                ],
                "pattern": "^(.*)$"
              },
              "Title": {
                "$id": "#/properties/Provider/properties/ProviderCMECredit/items/properties/Title",
                "type": "string",
                "title": "The Title Schema",
                "default": "",
                "examples": [
                  "Test"
                ],
                "pattern": "^(.*)$"
              },
              "LocationName": {
                "$id": "#/properties/Provider/properties/ProviderCMECredit/items/properties/LocationName",
                "type": "string",
                "title": "The Locationname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "StartDate": {
                "$id": "#/properties/Provider/properties/ProviderCMECredit/items/properties/StartDate",
                "type": "string",
                "title": "The Startdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EndDate": {
                "$id": "#/properties/Provider/properties/ProviderCMECredit/items/properties/EndDate",
                "type": "string",
                "title": "The Enddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderCoveringCollaborating": {
          "$id": "#/properties/Provider/properties/ProviderCoveringCollaborating",
          "type": "array",
          "title": "The Providercoveringcollaborating Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderCoveringCollaborating/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "TaxonomyCode",
              "CoveringProviderNPI",
              "CoveringStartDate",
              "CoveringEndDate",
              "CollaboratingAgreement"
            ],
            "properties": {
              "TaxonomyCode": {
                "$id": "#/properties/Provider/properties/ProviderCoveringCollaborating/items/properties/TaxonomyCode",
                "type": "string",
                "title": "The Taxonomycode Schema",
                "default": "",
                "examples": [
                  "207N00000X"
                ],
                "pattern": "^(.*)$"
              },
              "CoveringProviderNPI": {
                "$id": "#/properties/Provider/properties/ProviderCoveringCollaborating/items/properties/CoveringProviderNPI",
                "type": "string",
                "title": "The Coveringprovidernpi Schema",
                "default": "",
                "examples": [
                  "0016489149"
                ],
                "pattern": "^(.*)$"
              },
              "CoveringStartDate": {
                "$id": "#/properties/Provider/properties/ProviderCoveringCollaborating/items/properties/CoveringStartDate",
                "type": "string",
                "title": "The Coveringstartdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CoveringEndDate": {
                "$id": "#/properties/Provider/properties/ProviderCoveringCollaborating/items/properties/CoveringEndDate",
                "type": "string",
                "title": "The Coveringenddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CollaboratingAgreement": {
                "$id": "#/properties/Provider/properties/ProviderCoveringCollaborating/items/properties/CollaboratingAgreement",
                "type": "string",
                "title": "The Collaboratingagreement Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderEducationTraining": {
          "$id": "#/properties/Provider/properties/ProviderEducationTraining",
          "type": "array",
          "title": "The Providereducationtraining Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderEducationTraining/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "TaxonomyCode",
              "EducationTrainingType",
              "Degree",
              "DepartmentName",
              "EducationTrainingStartDate",
              "EducationTrainingEndDate",
              "ProgramDirectorName",
              "EducationTrainingIssueDate",
              "ResidentDatesFrom",
              "ResidentDatesTo",
              "ResidencyType",
              "Comments",
              "IsProgramCompleted",
              "SysAdminComment",
              "ECFMG",
              "InstitutionName",
              "TerminationReason",
              "TerminationDate",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "County",
              "CountryName",
              "Latitutde",
              "Longitude",
              "AddressWebsite",
              "AddressVerificationWebsite",
              "EMail",
              "Phone1",
              "Phone2",
              "Fax",
              "AddressNPI",
              "AddressComments"
            ],
            "properties": {
              "TaxonomyCode": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/TaxonomyCode",
                "type": "string",
                "title": "The Taxonomycode Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EducationTrainingType": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/EducationTrainingType",
                "type": "string",
                "title": "The Educationtrainingtype Schema",
                "default": "",
                "examples": [
                  "Dental School"
                ],
                "pattern": "^(.*)$"
              },
              "Degree": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Degree",
                "type": "string",
                "title": "The Degree Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DepartmentName": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/DepartmentName",
                "type": "string",
                "title": "The Departmentname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EducationTrainingStartDate": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/EducationTrainingStartDate",
                "type": "string",
                "title": "The Educationtrainingstartdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EducationTrainingEndDate": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/EducationTrainingEndDate",
                "type": "string",
                "title": "The Educationtrainingenddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ProgramDirectorName": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/ProgramDirectorName",
                "type": "string",
                "title": "The Programdirectorname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EducationTrainingIssueDate": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/EducationTrainingIssueDate",
                "type": "string",
                "title": "The Educationtrainingissuedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ResidentDatesFrom": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/ResidentDatesFrom",
                "type": "string",
                "title": "The Residentdatesfrom Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ResidentDatesTo": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/ResidentDatesTo",
                "type": "string",
                "title": "The Residentdatesto Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ResidencyType": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/ResidencyType",
                "type": "string",
                "title": "The Residencytype Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comments": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Comments",
                "type": "string",
                "title": "The Comments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsProgramCompleted": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/IsProgramCompleted",
                "type": "string",
                "title": "The Isprogramcompleted Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SysAdminComment": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/SysAdminComment",
                "type": "string",
                "title": "The Sysadmincomment Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ECFMG": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/ECFMG",
                "type": "string",
                "title": "The Ecfmg Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "InstitutionName": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/InstitutionName",
                "type": "string",
                "title": "The Institutionname Schema",
                "default": "",
                "examples": [
                  "Global Institute1 -  -  -  -  -  -  -  - "
                ],
                "pattern": "^(.*)$"
              },
              "TerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/TerminationReason",
                "type": "string",
                "title": "The Terminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationDate": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/TerminationDate",
                "type": "string",
                "title": "The Terminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CountryName": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/CountryName",
                "type": "string",
                "title": "The Countryname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressWebsite": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/AddressWebsite",
                "type": "string",
                "title": "The Addresswebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/AddressVerificationWebsite",
                "type": "string",
                "title": "The Addressverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EMail": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/EMail",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressNPI": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/AddressNPI",
                "type": "string",
                "title": "The Addressnpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressComments": {
                "$id": "#/properties/Provider/properties/ProviderEducationTraining/items/properties/AddressComments",
                "type": "string",
                "title": "The Addresscomments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderHealth": {
          "$id": "#/properties/Provider/properties/ProviderHealth",
          "type": "array",
          "title": "The Providerhealth Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderHealth/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "HealthType",
              "LastCheckupDate",
              "NextCheckupDate",
              "Result",
              "Comments"
            ],
            "properties": {
              "HealthType": {
                "$id": "#/properties/Provider/properties/ProviderHealth/items/properties/HealthType",
                "type": "string",
                "title": "The Healthtype Schema",
                "default": "",
                "examples": [
                  "Hepatitis B Vaccination"
                ],
                "pattern": "^(.*)$"
              },
              "LastCheckupDate": {
                "$id": "#/properties/Provider/properties/ProviderHealth/items/properties/LastCheckupDate",
                "type": "string",
                "title": "The Lastcheckupdate Schema",
                "default": "",
                "examples": [
                  "01/01/2018"
                ],
                "pattern": "^(.*)$"
              },
              "NextCheckupDate": {
                "$id": "#/properties/Provider/properties/ProviderHealth/items/properties/NextCheckupDate",
                "type": "string",
                "title": "The Nextcheckupdate Schema",
                "default": "",
                "examples": [
                  "12/31/2020"
                ],
                "pattern": "^(.*)$"
              },
              "Result": {
                "$id": "#/properties/Provider/properties/ProviderHealth/items/properties/Result",
                "type": "string",
                "title": "The Result Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comments": {
                "$id": "#/properties/Provider/properties/ProviderHealth/items/properties/Comments",
                "type": "string",
                "title": "The Comments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderHospitalPrivelege": {
          "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege",
          "type": "array",
          "title": "The Providerhospitalprivelege Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "TaxonomyCode",
              "HospitalPriviledegeStatus",
              "HospitalPrivelegeStaffCategory",
              "DepartmentChair",
              "Department",
              "AdmittingPrivilege",
              "PersentOfAdmission",
              "Comments",
              "PriviledegeName",
              "HospitalName",
              "TerminationReason",
              "TerminationDate",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "County",
              "CountryName",
              "Latitutde",
              "Longitude",
              "AddressWebsite",
              "AddressVerificationWebsite",
              "EMail",
              "Phone1",
              "Phone2",
              "Fax",
              "AddressNPI",
              "AddressComments"
            ],
            "properties": {
              "TaxonomyCode": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/TaxonomyCode",
                "type": "string",
                "title": "The Taxonomycode Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "HospitalPriviledegeStatus": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/HospitalPriviledegeStatus",
                "type": "string",
                "title": "The Hospitalpriviledegestatus Schema",
                "default": "",
                "examples": [
                  "Full Privileges"
                ],
                "pattern": "^(.*)$"
              },
              "HospitalPrivelegeStaffCategory": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/HospitalPrivelegeStaffCategory",
                "type": "string",
                "title": "The Hospitalprivelegestaffcategory Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DepartmentChair": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/DepartmentChair",
                "type": "string",
                "title": "The Departmentchair Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Department": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Department",
                "type": "string",
                "title": "The Department Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AdmittingPrivilege": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/AdmittingPrivilege",
                "type": "string",
                "title": "The Admittingprivilege Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PersentOfAdmission": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/PersentOfAdmission",
                "type": "string",
                "title": "The Persentofadmission Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comments": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Comments",
                "type": "string",
                "title": "The Comments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PriviledegeName": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/PriviledegeName",
                "type": "string",
                "title": "The Priviledegename Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "HospitalName": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/HospitalName",
                "type": "string",
                "title": "The Hospitalname Schema",
                "default": "",
                "examples": [
                  "MahatmaGandhi"
                ],
                "pattern": "^(.*)$"
              },
              "TerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/TerminationReason",
                "type": "string",
                "title": "The Terminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationDate": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/TerminationDate",
                "type": "string",
                "title": "The Terminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CountryName": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/CountryName",
                "type": "string",
                "title": "The Countryname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressWebsite": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/AddressWebsite",
                "type": "string",
                "title": "The Addresswebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/AddressVerificationWebsite",
                "type": "string",
                "title": "The Addressverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EMail": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/EMail",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressNPI": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/AddressNPI",
                "type": "string",
                "title": "The Addressnpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressComments": {
                "$id": "#/properties/Provider/properties/ProviderHospitalPrivelege/items/properties/AddressComments",
                "type": "string",
                "title": "The Addresscomments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderLanguages": {
          "$id": "#/properties/Provider/properties/ProviderLanguages",
          "type": "array",
          "title": "The Providerlanguages Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderLanguages/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "Language",
              "LanguageCode",
              "Read",
              "Write",
              "Speak"
            ],
            "properties": {
              "Language": {
                "$id": "#/properties/Provider/properties/ProviderLanguages/items/properties/Language",
                "type": "string",
                "title": "The Language Schema",
                "default": "",
                "examples": [
                  "English"
                ],
                "pattern": "^(.*)$"
              },
              "LanguageCode": {
                "$id": "#/properties/Provider/properties/ProviderLanguages/items/properties/LanguageCode",
                "type": "string",
                "title": "The Languagecode Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Read": {
                "$id": "#/properties/Provider/properties/ProviderLanguages/items/properties/Read",
                "type": "string",
                "title": "The Read Schema",
                "default": "",
                "examples": [
                  "Yes"
                ],
                "pattern": "^(.*)$"
              },
              "Write": {
                "$id": "#/properties/Provider/properties/ProviderLanguages/items/properties/Write",
                "type": "string",
                "title": "The Write Schema",
                "default": "",
                "examples": [
                  "Yes"
                ],
                "pattern": "^(.*)$"
              },
              "Speak": {
                "$id": "#/properties/Provider/properties/ProviderLanguages/items/properties/Speak",
                "type": "string",
                "title": "The Speak Schema",
                "default": "",
                "examples": [
                  "Yes"
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderMalPractice": {
          "$id": "#/properties/Provider/properties/ProviderMalPractice",
          "type": "array",
          "title": "The Providermalpractice Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderMalPractice/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "PrimaryInsuranceCarrier",
              "ExcessInsuranceCarrier",
              "MalpracticeDefendantType",
              "MalpracticeDefendantCategory",
              "MalpracticeCaseStatus",
              "MalpracticePaymentType",
              "PrimaryInsuranceCarrierReportedDate",
              "ExcessInsuranceCarrierReportedDate",
              "CourtFileNumber",
              "LawsuitFieldDate",
              "ActOccurrenceDate",
              "ActOccurrenceLocation",
              "ActOccurred",
              "ActDescription",
              "CoDefendants",
              "CaseStatusComment",
              "IncidentFiledDate",
              "IncidentDate",
              "IncidentLocation",
              "Incident",
              "IncidentDescription",
              "Comment",
              "JudgmentDate",
              "JudgmentDescription",
              "Amount",
              "PaymentDate",
              "PaymentResult",
              "NumberOfPayor",
              "IsNPDBReport",
              "ClaimentFirstName",
              "ClaimentLastName",
              "ClaimentSex",
              "ClaimentDOB",
              "SubsequentCondition",
              "AttorneyFirstName",
              "AttorneyLastName",
              "AllegedHarmPatient",
              "AllegedHaveIncorrectlyFailed",
              "PatientIllnessRelatedEffectsAllegedHarms",
              "OtherDetailsBelievePertinentCase",
              "OtherPartiesNamedInSuit",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "County",
              "CountryName",
              "Latitutde",
              "Longitude",
              "Phone"
            ],
            "properties": {
              "PrimaryInsuranceCarrier": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/PrimaryInsuranceCarrier",
                "type": "string",
                "title": "The Primaryinsurancecarrier Schema",
                "default": "",
                "examples": [
                  "Excess Carrier-India"
                ],
                "pattern": "^(.*)$"
              },
              "ExcessInsuranceCarrier": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ExcessInsuranceCarrier",
                "type": "string",
                "title": "The Excessinsurancecarrier Schema",
                "default": "",
                "examples": [
                  "Excess Carrier 11111-USA"
                ],
                "pattern": "^(.*)$"
              },
              "MalpracticeDefendantType": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/MalpracticeDefendantType",
                "type": "string",
                "title": "The Malpracticedefendanttype Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MalpracticeDefendantCategory": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/MalpracticeDefendantCategory",
                "type": "string",
                "title": "The Malpracticedefendantcategory Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MalpracticeCaseStatus": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/MalpracticeCaseStatus",
                "type": "string",
                "title": "The Malpracticecasestatus Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MalpracticePaymentType": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/MalpracticePaymentType",
                "type": "string",
                "title": "The Malpracticepaymenttype Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryInsuranceCarrierReportedDate": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/PrimaryInsuranceCarrierReportedDate",
                "type": "string",
                "title": "The Primaryinsurancecarrierreporteddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ExcessInsuranceCarrierReportedDate": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ExcessInsuranceCarrierReportedDate",
                "type": "string",
                "title": "The Excessinsurancecarrierreporteddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CourtFileNumber": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/CourtFileNumber",
                "type": "string",
                "title": "The Courtfilenumber Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "LawsuitFieldDate": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/LawsuitFieldDate",
                "type": "string",
                "title": "The Lawsuitfielddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ActOccurrenceDate": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ActOccurrenceDate",
                "type": "string",
                "title": "The Actoccurrencedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ActOccurrenceLocation": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ActOccurrenceLocation",
                "type": "string",
                "title": "The Actoccurrencelocation Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ActOccurred": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ActOccurred",
                "type": "string",
                "title": "The Actoccurred Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ActDescription": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ActDescription",
                "type": "string",
                "title": "The Actdescription Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CoDefendants": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/CoDefendants",
                "type": "string",
                "title": "The Codefendants Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CaseStatusComment": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/CaseStatusComment",
                "type": "string",
                "title": "The Casestatuscomment Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IncidentFiledDate": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/IncidentFiledDate",
                "type": "string",
                "title": "The Incidentfileddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IncidentDate": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/IncidentDate",
                "type": "string",
                "title": "The Incidentdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IncidentLocation": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/IncidentLocation",
                "type": "string",
                "title": "The Incidentlocation Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Incident": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Incident",
                "type": "string",
                "title": "The Incident Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IncidentDescription": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/IncidentDescription",
                "type": "string",
                "title": "The Incidentdescription Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comment": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Comment",
                "type": "string",
                "title": "The Comment Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "JudgmentDate": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/JudgmentDate",
                "type": "string",
                "title": "The Judgmentdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "JudgmentDescription": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/JudgmentDescription",
                "type": "string",
                "title": "The Judgmentdescription Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Amount": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Amount",
                "type": "string",
                "title": "The Amount Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PaymentDate": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/PaymentDate",
                "type": "string",
                "title": "The Paymentdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PaymentResult": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/PaymentResult",
                "type": "string",
                "title": "The Paymentresult Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "NumberOfPayor": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/NumberOfPayor",
                "type": "string",
                "title": "The Numberofpayor Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsNPDBReport": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/IsNPDBReport",
                "type": "string",
                "title": "The Isnpdbreport Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ClaimentFirstName": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ClaimentFirstName",
                "type": "string",
                "title": "The Claimentfirstname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ClaimentLastName": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ClaimentLastName",
                "type": "string",
                "title": "The Claimentlastname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ClaimentSex": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ClaimentSex",
                "type": "string",
                "title": "The Claimentsex Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ClaimentDOB": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/ClaimentDOB",
                "type": "string",
                "title": "The Claimentdob Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SubsequentCondition": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/SubsequentCondition",
                "type": "string",
                "title": "The Subsequentcondition Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AttorneyFirstName": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/AttorneyFirstName",
                "type": "string",
                "title": "The Attorneyfirstname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AttorneyLastName": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/AttorneyLastName",
                "type": "string",
                "title": "The Attorneylastname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AllegedHarmPatient": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/AllegedHarmPatient",
                "type": "string",
                "title": "The Allegedharmpatient Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AllegedHaveIncorrectlyFailed": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/AllegedHaveIncorrectlyFailed",
                "type": "string",
                "title": "The Allegedhaveincorrectlyfailed Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PatientIllnessRelatedEffectsAllegedHarms": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/PatientIllnessRelatedEffectsAllegedHarms",
                "type": "string",
                "title": "The Patientillnessrelatedeffectsallegedharms Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "OtherDetailsBelievePertinentCase": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/OtherDetailsBelievePertinentCase",
                "type": "string",
                "title": "The Otherdetailsbelievepertinentcase Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "OtherPartiesNamedInSuit": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/OtherPartiesNamedInSuit",
                "type": "string",
                "title": "The Otherpartiesnamedinsuit Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CountryName": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/CountryName",
                "type": "string",
                "title": "The Countryname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone": {
                "$id": "#/properties/Provider/properties/ProviderMalPractice/items/properties/Phone",
                "type": "string",
                "title": "The Phone Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderOtherIdType": {
          "$id": "#/properties/Provider/properties/ProviderOtherIdType",
          "type": "array",
          "title": "The Providerotheridtype Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderOtherIdType/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "OtherIdType",
              "OtherIdNumber",
              "StartDate",
              "ExpirationDate",
              "OtherIdUserId",
              "OtherIdPassword",
              "Notes",
              "State",
              "CallCAQH"
            ],
            "properties": {
              "OtherIdType": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/OtherIdType",
                "type": "string",
                "title": "The Otheridtype Schema",
                "default": "",
                "examples": [
                  "CAQH"
                ],
                "pattern": "^(.*)$"
              },
              "OtherIdNumber": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/OtherIdNumber",
                "type": "string",
                "title": "The Otheridnumber Schema",
                "default": "",
                "examples": [
                  "124578"
                ],
                "pattern": "^(.*)$"
              },
              "StartDate": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/StartDate",
                "type": "string",
                "title": "The Startdate Schema",
                "default": "",
                "examples": [
                  "01/01/2019"
                ],
                "pattern": "^(.*)$"
              },
              "ExpirationDate": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/ExpirationDate",
                "type": "string",
                "title": "The Expirationdate Schema",
                "default": "",
                "examples": [
                  "12/31/2021"
                ],
                "pattern": "^(.*)$"
              },
              "OtherIdUserId": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/OtherIdUserId",
                "type": "string",
                "title": "The Otheriduserid Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "OtherIdPassword": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/OtherIdPassword",
                "type": "string",
                "title": "The Otheridpassword Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Notes": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/Notes",
                "type": "string",
                "title": "The Notes Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CallCAQH": {
                "$id": "#/properties/Provider/properties/ProviderOtherIdType/items/properties/CallCAQH",
                "type": "string",
                "title": "The Callcaqh Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderReference": {
          "$id": "#/properties/Provider/properties/ProviderReference",
          "type": "array",
          "title": "The Providerreference Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderReference/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "TaxonomyCode",
              "FirstName",
              "LastName",
              "Title",
              "Suffix",
              "RelationShip",
              "DateAdded",
              "AddressName",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "County",
              "CountryName",
              "Latitutde",
              "Longitude",
              "EMail",
              "Phone1",
              "Phone2",
              "Fax"
            ],
            "properties": {
              "TaxonomyCode": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/TaxonomyCode",
                "type": "string",
                "title": "The Taxonomycode Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FirstName": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/FirstName",
                "type": "string",
                "title": "The Firstname Schema",
                "default": "",
                "examples": [
                  "RefFirst"
                ],
                "pattern": "^(.*)$"
              },
              "LastName": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/LastName",
                "type": "string",
                "title": "The Lastname Schema",
                "default": "",
                "examples": [
                  "RefLast"
                ],
                "pattern": "^(.*)$"
              },
              "Title": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Title",
                "type": "string",
                "title": "The Title Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Suffix": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Suffix",
                "type": "string",
                "title": "The Suffix Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "RelationShip": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/RelationShip",
                "type": "string",
                "title": "The Relationship Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DateAdded": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/DateAdded",
                "type": "string",
                "title": "The Dateadded Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressName": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/AddressName",
                "type": "string",
                "title": "The Addressname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CountryName": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/CountryName",
                "type": "string",
                "title": "The Countryname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EMail": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/EMail",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderReference/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderEmploymentHistory": {
          "$id": "#/properties/Provider/properties/ProviderEmploymentHistory",
          "type": "array",
          "title": "The Provideremploymenthistory Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "TaxonomyCode",
              "EmployerName",
              "EmploymentId",
              "TerminationReason",
              "TerminatedDate",
              "Department",
              "EmployerProviderDesignation",
              "Explanation",
              "SysAdminComment",
              "StartDate",
              "EndDate",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "County",
              "CountryName",
              "Latitutde",
              "Longitude",
              "AddressWebsite",
              "AddressVerificationWebsite",
              "EMail",
              "Phone1",
              "Phone2",
              "Fax",
              "AddressNPI",
              "AddressComments"
            ],
            "properties": {
              "TaxonomyCode": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/TaxonomyCode",
                "type": "string",
                "title": "The Taxonomycode Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EmployerName": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/EmployerName",
                "type": "string",
                "title": "The Employername Schema",
                "default": "",
                "examples": [
                  "New employer testing master"
                ],
                "pattern": "^(.*)$"
              },
              "EmploymentId": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/EmploymentId",
                "type": "string",
                "title": "The Employmentid Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/TerminationReason",
                "type": "string",
                "title": "The Terminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminatedDate": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/TerminatedDate",
                "type": "string",
                "title": "The Terminateddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Department": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Department",
                "type": "string",
                "title": "The Department Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EmployerProviderDesignation": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/EmployerProviderDesignation",
                "type": "string",
                "title": "The Employerproviderdesignation Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Explanation": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Explanation",
                "type": "string",
                "title": "The Explanation Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SysAdminComment": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/SysAdminComment",
                "type": "string",
                "title": "The Sysadmincomment Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "StartDate": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/StartDate",
                "type": "string",
                "title": "The Startdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EndDate": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/EndDate",
                "type": "string",
                "title": "The Enddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CountryName": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/CountryName",
                "type": "string",
                "title": "The Countryname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressWebsite": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/AddressWebsite",
                "type": "string",
                "title": "The Addresswebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressVerificationWebsite": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/AddressVerificationWebsite",
                "type": "string",
                "title": "The Addressverificationwebsite Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EMail": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/EMail",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressNPI": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/AddressNPI",
                "type": "string",
                "title": "The Addressnpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressComments": {
                "$id": "#/properties/Provider/properties/ProviderEmploymentHistory/items/properties/AddressComments",
                "type": "string",
                "title": "The Addresscomments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "Practice": {
          "$id": "#/properties/Provider/properties/Practice",
          "type": "array",
          "title": "The Practice Schema",
          "items": {
            "$id": "#/properties/Provider/properties/Practice/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "PracticeName",
              "TaxID",
              "GroupNpi",
              "Phone",
              "Fax",
              "Email",
              "PracticeAdmin",
              "DbaName",
              "PracticeType",
              "TinEffectiveDate",
              "NpiEffectiveDate",
              "RecredCycle",
              "CredentialName",
              "CredentialPhone",
              "CredentialFax",
              "CredentialEmail",
              "PhoneExtension",
              "CredentialPhoneExtension",
              "CredentialFaxExtension",
              "IsDummyTaxId",
              "TerminationDate",
              "TerminationReason",
              "PrvPracticeEffectiveDate",
              "PrvPracticeTerminationDate",
              "PrvPracticeTerminationReason"
            ],
            "properties": {
              "PracticeName": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/PracticeName",
                "type": "string",
                "title": "The Practicename Schema",
                "default": "",
                "examples": [
                  "Meridian Behavioral Healthcare Inc"
                ],
                "pattern": "^(.*)$"
              },
              "TaxID": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/TaxID",
                "type": "string",
                "title": "The Taxid Schema",
                "default": "",
                "examples": [
                  "814789658"
                ],
                "pattern": "^(.*)$"
              },
              "GroupNpi": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/GroupNpi",
                "type": "string",
                "title": "The Groupnpi Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/Phone",
                "type": "string",
                "title": "The Phone Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Email": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/Email",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PracticeAdmin": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/PracticeAdmin",
                "type": "string",
                "title": "The Practiceadmin Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DbaName": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/DbaName",
                "type": "string",
                "title": "The Dbaname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PracticeType": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/PracticeType",
                "type": "string",
                "title": "The Practicetype Schema",
                "default": "",
                "examples": [
                  "Sole Proprietership"
                ],
                "pattern": "^(.*)$"
              },
              "TinEffectiveDate": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/TinEffectiveDate",
                "type": "string",
                "title": "The Tineffectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "NpiEffectiveDate": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/NpiEffectiveDate",
                "type": "string",
                "title": "The Npieffectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "RecredCycle": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/RecredCycle",
                "type": "string",
                "title": "The Recredcycle Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CredentialName": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/CredentialName",
                "type": "string",
                "title": "The Credentialname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CredentialPhone": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/CredentialPhone",
                "type": "string",
                "title": "The Credentialphone Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CredentialFax": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/CredentialFax",
                "type": "string",
                "title": "The Credentialfax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CredentialEmail": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/CredentialEmail",
                "type": "string",
                "title": "The Credentialemail Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PhoneExtension": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/PhoneExtension",
                "type": "string",
                "title": "The Phoneextension Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CredentialPhoneExtension": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/CredentialPhoneExtension",
                "type": "string",
                "title": "The Credentialphoneextension Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CredentialFaxExtension": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/CredentialFaxExtension",
                "type": "string",
                "title": "The Credentialfaxextension Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsDummyTaxId": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/IsDummyTaxId",
                "type": "string",
                "title": "The Isdummytaxid Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationDate": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/TerminationDate",
                "type": "string",
                "title": "The Terminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationReason": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/TerminationReason",
                "type": "string",
                "title": "The Terminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrvPracticeEffectiveDate": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/PrvPracticeEffectiveDate",
                "type": "string",
                "title": "The Prvpracticeeffectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrvPracticeTerminationDate": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/PrvPracticeTerminationDate",
                "type": "string",
                "title": "The Prvpracticeterminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrvPracticeTerminationReason": {
                "$id": "#/properties/Provider/properties/Practice/items/properties/PrvPracticeTerminationReason",
                "type": "string",
                "title": "The Prvpracticeterminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "PracticeLocation": {
          "$id": "#/properties/Provider/properties/PracticeLocation",
          "type": "array",
          "title": "The Practicelocation Schema",
          "items": {
            "$id": "#/properties/Provider/properties/PracticeLocation/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "TaxID",
              "LocationEffectiveDate",
              "LocationTerminationDate",
              "LocationContactName",
              "LocationContactEmail",
              "LocationTerminationReason",
              "AddressName",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "County",
              "Country",
              "Latitutde",
              "Longitude",
              "IsVerified",
              "ConfidenceLevel",
              "Website",
              "Email",
              "Phone1",
              "Phone1Extension",
              "Phone1ISDCode",
              "Phone2",
              "Phone2Extension",
              "Phone2ISDCode",
              "Fax",
              "FaxExtension",
              "FaxISDCode",
              "ContactPersonName",
              "ContactDepartment",
              "ContactTitle",
              "Comments",
              "MondayOpenHour",
              "MondayLunchFromHour",
              "MondayLunchToHour",
              "MondayCloseHour",
              "TuesdayOpenHour",
              "TuesdayLunchFromHour",
              "TuesdayLunchToHour",
              "TuesdayCloseHour",
              "WednesdayOpenHour",
              "WednesdayLunchFromHour",
              "WednesdayLunchToHour",
              "WednesdayCloseHour",
              "ThursdayOpenHour",
              "ThursdayLunchFromHour",
              "ThursdayLunchToHour",
              "ThursdayCloseHour",
              "FridayOpenHour",
              "FridayLunchFromHour",
              "FridayLunchToHour",
              "FridayCloseHour",
              "SaturdayOpenHour",
              "SaturdayLunchFromHour",
              "SaturdayLunchToHour",
              "SaturdayCloseHour",
              "SundayOpenHour",
              "SundayLunchFromHour",
              "SundayLunchToHour",
              "SundayCloseHour"
            ],
            "properties": {
              "TaxID": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/TaxID",
                "type": "string",
                "title": "The Taxid Schema",
                "default": "",
                "examples": [
                  "814789658"
                ],
                "pattern": "^(.*)$"
              },
              "LocationEffectiveDate": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/LocationEffectiveDate",
                "type": "string",
                "title": "The Locationeffectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "LocationTerminationDate": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/LocationTerminationDate",
                "type": "string",
                "title": "The Locationterminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "LocationContactName": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/LocationContactName",
                "type": "string",
                "title": "The Locationcontactname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "LocationContactEmail": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/LocationContactEmail",
                "type": "string",
                "title": "The Locationcontactemail Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "LocationTerminationReason": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/LocationTerminationReason",
                "type": "string",
                "title": "The Locationterminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AddressName": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/AddressName",
                "type": "string",
                "title": "The Addressname Schema",
                "default": "",
                "examples": [
                  "Meridian Behavioral Healthcare Inc"
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  "92 W Lowder St Macclenny"
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  "Jacksonville"
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  "NC"
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  "32063"
                ],
                "pattern": "^(.*)$"
              },
              "County": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/County",
                "type": "string",
                "title": "The County Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Country": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Country",
                "type": "string",
                "title": "The Country Schema",
                "default": "",
                "examples": [
                  "USA"
                ],
                "pattern": "^(.*)$"
              },
              "Latitutde": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Latitutde",
                "type": "string",
                "title": "The Latitutde Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Longitude": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Longitude",
                "type": "string",
                "title": "The Longitude Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsVerified": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/IsVerified",
                "type": "string",
                "title": "The Isverified Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ConfidenceLevel": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/ConfidenceLevel",
                "type": "string",
                "title": "The Confidencelevel Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Website": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Website",
                "type": "string",
                "title": "The Website Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Email": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Email",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  "msb.net.in@gmail.com"
                ],
                "pattern": "^(.*)$"
              },
              "Phone1": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Phone1",
                "type": "string",
                "title": "The Phone1 Schema",
                "default": "",
                "examples": [
                  "9829529565"
                ],
                "pattern": "^(.*)$"
              },
              "Phone1Extension": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Phone1Extension",
                "type": "string",
                "title": "The Phone1extension Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone1ISDCode": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Phone1ISDCode",
                "type": "string",
                "title": "The Phone1isdcode Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Phone2",
                "type": "string",
                "title": "The Phone2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2Extension": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Phone2Extension",
                "type": "string",
                "title": "The Phone2extension Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Phone2ISDCode": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Phone2ISDCode",
                "type": "string",
                "title": "The Phone2isdcode Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FaxExtension": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/FaxExtension",
                "type": "string",
                "title": "The Faxextension Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FaxISDCode": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/FaxISDCode",
                "type": "string",
                "title": "The Faxisdcode Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ContactPersonName": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/ContactPersonName",
                "type": "string",
                "title": "The Contactpersonname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ContactDepartment": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/ContactDepartment",
                "type": "string",
                "title": "The Contactdepartment Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ContactTitle": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/ContactTitle",
                "type": "string",
                "title": "The Contacttitle Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comments": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/Comments",
                "type": "string",
                "title": "The Comments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MondayOpenHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/MondayOpenHour",
                "type": "string",
                "title": "The Mondayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MondayLunchFromHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/MondayLunchFromHour",
                "type": "string",
                "title": "The Mondaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MondayLunchToHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/MondayLunchToHour",
                "type": "string",
                "title": "The Mondaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MondayCloseHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/MondayCloseHour",
                "type": "string",
                "title": "The Mondayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TuesdayOpenHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/TuesdayOpenHour",
                "type": "string",
                "title": "The Tuesdayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TuesdayLunchFromHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/TuesdayLunchFromHour",
                "type": "string",
                "title": "The Tuesdaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TuesdayLunchToHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/TuesdayLunchToHour",
                "type": "string",
                "title": "The Tuesdaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TuesdayCloseHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/TuesdayCloseHour",
                "type": "string",
                "title": "The Tuesdayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WednesdayOpenHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/WednesdayOpenHour",
                "type": "string",
                "title": "The Wednesdayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WednesdayLunchFromHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/WednesdayLunchFromHour",
                "type": "string",
                "title": "The Wednesdaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WednesdayLunchToHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/WednesdayLunchToHour",
                "type": "string",
                "title": "The Wednesdaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WednesdayCloseHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/WednesdayCloseHour",
                "type": "string",
                "title": "The Wednesdayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ThursdayOpenHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/ThursdayOpenHour",
                "type": "string",
                "title": "The Thursdayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ThursdayLunchFromHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/ThursdayLunchFromHour",
                "type": "string",
                "title": "The Thursdaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ThursdayLunchToHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/ThursdayLunchToHour",
                "type": "string",
                "title": "The Thursdaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ThursdayCloseHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/ThursdayCloseHour",
                "type": "string",
                "title": "The Thursdayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FridayOpenHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/FridayOpenHour",
                "type": "string",
                "title": "The Fridayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FridayLunchFromHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/FridayLunchFromHour",
                "type": "string",
                "title": "The Fridaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FridayLunchToHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/FridayLunchToHour",
                "type": "string",
                "title": "The Fridaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FridayCloseHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/FridayCloseHour",
                "type": "string",
                "title": "The Fridayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SaturdayOpenHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/SaturdayOpenHour",
                "type": "string",
                "title": "The Saturdayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SaturdayLunchFromHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/SaturdayLunchFromHour",
                "type": "string",
                "title": "The Saturdaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SaturdayLunchToHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/SaturdayLunchToHour",
                "type": "string",
                "title": "The Saturdaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SaturdayCloseHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/SaturdayCloseHour",
                "type": "string",
                "title": "The Saturdayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SundayOpenHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/SundayOpenHour",
                "type": "string",
                "title": "The Sundayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SundayLunchFromHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/SundayLunchFromHour",
                "type": "string",
                "title": "The Sundaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SundayLunchToHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/SundayLunchToHour",
                "type": "string",
                "title": "The Sundaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SundayCloseHour": {
                "$id": "#/properties/Provider/properties/PracticeLocation/items/properties/SundayCloseHour",
                "type": "string",
                "title": "The Sundayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderPracticeLocation": {
          "$id": "#/properties/Provider/properties/ProviderPracticeLocation",
          "type": "array",
          "title": "The Providerpracticelocation Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "TaxID",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "TerminationDate",
              "TerminationReason",
              "PrimaryEffectiveDate",
              "PrimaryTerminationDate",
              "PrimaryTerminationReason",
              "OfficeEmployeeType",
              "PositionName",
              "JobType",
              "ConfidentialHire",
              "Title",
              "FirstName",
              "MiddleName",
              "LastName",
              "Suffix",
              "Email",
              "Phone",
              "PhoneExtension",
              "Fax",
              "FaxExtension",
              "DirectorName",
              "RecruiterName",
              "WeekendHours",
              "EveningHours",
              "UndefinedHours",
              "DateOfHiring",
              "EffectiveDate",
              "RecredentialDate",
              "MondayOpenHour",
              "MondayLunchFromHour",
              "MondayLunchToHour",
              "MondayCloseHour",
              "TuesdayOpenHour",
              "TuesdayLunchFromHour",
              "TuesdayLunchToHour",
              "TuesdayCloseHour",
              "WednesdayOpenHour",
              "WednesdayLunchFromHour",
              "WednesdayLunchToHour",
              "WednesdayCloseHour",
              "ThursdayOpenHour",
              "ThursdayLunchFromHour",
              "ThursdayLunchToHour",
              "ThursdayCloseHour",
              "FridayOpenHour",
              "FridayLunchFromHour",
              "FridayLunchToHour",
              "FridayCloseHour",
              "SaturdayOpenHour",
              "SaturdayLunchFromHour",
              "SaturdayLunchToHour",
              "SaturdayCloseHour",
              "SundayOpenHour",
              "SundayLunchFromHour",
              "SundayLunchToHour",
              "SundayCloseHour"
            ],
            "properties": {
              "TaxID": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/TaxID",
                "type": "string",
                "title": "The Taxid Schema",
                "default": "",
                "examples": [
                  "814789658"
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  "92 W Lowder St Macclenny"
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  "Jacksonville"
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  "NC"
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  "32063"
                ],
                "pattern": "^(.*)$"
              },
              "TerminationDate": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/TerminationDate",
                "type": "string",
                "title": "The Terminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/TerminationReason",
                "type": "string",
                "title": "The Terminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryEffectiveDate": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/PrimaryEffectiveDate",
                "type": "string",
                "title": "The Primaryeffectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryTerminationDate": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/PrimaryTerminationDate",
                "type": "string",
                "title": "The Primaryterminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PrimaryTerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/PrimaryTerminationReason",
                "type": "string",
                "title": "The Primaryterminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "OfficeEmployeeType": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/OfficeEmployeeType",
                "type": "string",
                "title": "The Officeemployeetype Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PositionName": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/PositionName",
                "type": "string",
                "title": "The Positionname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "JobType": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/JobType",
                "type": "string",
                "title": "The Jobtype Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ConfidentialHire": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/ConfidentialHire",
                "type": "string",
                "title": "The Confidentialhire Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Title": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/Title",
                "type": "string",
                "title": "The Title Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FirstName": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/FirstName",
                "type": "string",
                "title": "The Firstname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MiddleName": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/MiddleName",
                "type": "string",
                "title": "The Middlename Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "LastName": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/LastName",
                "type": "string",
                "title": "The Lastname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Suffix": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/Suffix",
                "type": "string",
                "title": "The Suffix Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Email": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/Email",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  "msb.net.in@gmail.com"
                ],
                "pattern": "^(.*)$"
              },
              "Phone": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/Phone",
                "type": "string",
                "title": "The Phone Schema",
                "default": "",
                "examples": [
                  "9829529565"
                ],
                "pattern": "^(.*)$"
              },
              "PhoneExtension": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/PhoneExtension",
                "type": "string",
                "title": "The Phoneextension Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Fax": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/Fax",
                "type": "string",
                "title": "The Fax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FaxExtension": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/FaxExtension",
                "type": "string",
                "title": "The Faxextension Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DirectorName": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/DirectorName",
                "type": "string",
                "title": "The Directorname Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "RecruiterName": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/RecruiterName",
                "type": "string",
                "title": "The Recruitername Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WeekendHours": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/WeekendHours",
                "type": "string",
                "title": "The Weekendhours Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EveningHours": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/EveningHours",
                "type": "string",
                "title": "The Eveninghours Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "UndefinedHours": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/UndefinedHours",
                "type": "string",
                "title": "The Undefinedhours Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DateOfHiring": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/DateOfHiring",
                "type": "string",
                "title": "The Dateofhiring Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "EffectiveDate": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/EffectiveDate",
                "type": "string",
                "title": "The Effectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "RecredentialDate": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/RecredentialDate",
                "type": "string",
                "title": "The Recredentialdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MondayOpenHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/MondayOpenHour",
                "type": "string",
                "title": "The Mondayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MondayLunchFromHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/MondayLunchFromHour",
                "type": "string",
                "title": "The Mondaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MondayLunchToHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/MondayLunchToHour",
                "type": "string",
                "title": "The Mondaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "MondayCloseHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/MondayCloseHour",
                "type": "string",
                "title": "The Mondayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TuesdayOpenHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/TuesdayOpenHour",
                "type": "string",
                "title": "The Tuesdayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TuesdayLunchFromHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/TuesdayLunchFromHour",
                "type": "string",
                "title": "The Tuesdaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TuesdayLunchToHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/TuesdayLunchToHour",
                "type": "string",
                "title": "The Tuesdaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TuesdayCloseHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/TuesdayCloseHour",
                "type": "string",
                "title": "The Tuesdayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WednesdayOpenHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/WednesdayOpenHour",
                "type": "string",
                "title": "The Wednesdayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WednesdayLunchFromHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/WednesdayLunchFromHour",
                "type": "string",
                "title": "The Wednesdaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WednesdayLunchToHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/WednesdayLunchToHour",
                "type": "string",
                "title": "The Wednesdaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "WednesdayCloseHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/WednesdayCloseHour",
                "type": "string",
                "title": "The Wednesdayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ThursdayOpenHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/ThursdayOpenHour",
                "type": "string",
                "title": "The Thursdayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ThursdayLunchFromHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/ThursdayLunchFromHour",
                "type": "string",
                "title": "The Thursdaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ThursdayLunchToHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/ThursdayLunchToHour",
                "type": "string",
                "title": "The Thursdaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ThursdayCloseHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/ThursdayCloseHour",
                "type": "string",
                "title": "The Thursdayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FridayOpenHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/FridayOpenHour",
                "type": "string",
                "title": "The Fridayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FridayLunchFromHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/FridayLunchFromHour",
                "type": "string",
                "title": "The Fridaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FridayLunchToHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/FridayLunchToHour",
                "type": "string",
                "title": "The Fridaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "FridayCloseHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/FridayCloseHour",
                "type": "string",
                "title": "The Fridayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SaturdayOpenHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/SaturdayOpenHour",
                "type": "string",
                "title": "The Saturdayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SaturdayLunchFromHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/SaturdayLunchFromHour",
                "type": "string",
                "title": "The Saturdaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SaturdayLunchToHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/SaturdayLunchToHour",
                "type": "string",
                "title": "The Saturdaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SaturdayCloseHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/SaturdayCloseHour",
                "type": "string",
                "title": "The Saturdayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SundayOpenHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/SundayOpenHour",
                "type": "string",
                "title": "The Sundayopenhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SundayLunchFromHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/SundayLunchFromHour",
                "type": "string",
                "title": "The Sundaylunchfromhour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SundayLunchToHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/SundayLunchToHour",
                "type": "string",
                "title": "The Sundaylunchtohour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SundayCloseHour": {
                "$id": "#/properties/Provider/properties/ProviderPracticeLocation/items/properties/SundayCloseHour",
                "type": "string",
                "title": "The Sundayclosehour Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderContractLine": {
          "$id": "#/properties/Provider/properties/ProviderContractLine",
          "type": "array",
          "title": "The Providercontractline Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderContractLine/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "NetworkName",
              "SubNetworkName",
              "TaxID",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "TaxonomyCode",
              "EffectiveDate",
              "TerminationDate",
              "TerminationReason",
              "PushToDirectory",
              "PushToClaim",
              "AcceptingNewPatient",
              "LastVerifiedDate",
              "PatientAgeLimitMin",
              "PatientAgeLimitMax",
              "IsVerified",
              "SubNetworkPracticeEffectiveDate",
              "SubNetworkPracticeTerminateDate",
              "IsDelegated",
              "DelegatedEffectiveDate",
              "DelegatedTerminationDate",
              "DelegatedTerminationReason"
            ],
            "properties": {
              "NetworkName": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/NetworkName",
                "type": "string",
                "title": "The Networkname Schema",
                "default": "",
                "examples": [
                  "LTC Meridian"
                ],
                "pattern": "^(.*)$"
              },
              "SubNetworkName": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/SubNetworkName",
                "type": "string",
                "title": "The Subnetworkname Schema",
                "default": "",
                "examples": [
                  "Sub- LTC Meridian"
                ],
                "pattern": "^(.*)$"
              },
              "TaxID": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/TaxID",
                "type": "string",
                "title": "The Taxid Schema",
                "default": "",
                "examples": [
                  "814789658"
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  "92 W Lowder St Macclenny"
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  "Jacksonville"
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  "NC"
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  "32063"
                ],
                "pattern": "^(.*)$"
              },
              "TaxonomyCode": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/TaxonomyCode",
                "type": "string",
                "title": "The Taxonomycode Schema",
                "default": "",
                "examples": [
                  "1223D0004X"
                ],
                "pattern": "^(.*)$"
              },
              "EffectiveDate": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/EffectiveDate",
                "type": "string",
                "title": "The Effectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationDate": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/TerminationDate",
                "type": "string",
                "title": "The Terminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "TerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/TerminationReason",
                "type": "string",
                "title": "The Terminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PushToDirectory": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/PushToDirectory",
                "type": "string",
                "title": "The Pushtodirectory Schema",
                "default": "",
                "examples": [
                  "No"
                ],
                "pattern": "^(.*)$"
              },
              "PushToClaim": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/PushToClaim",
                "type": "string",
                "title": "The Pushtoclaim Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "AcceptingNewPatient": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/AcceptingNewPatient",
                "type": "string",
                "title": "The Acceptingnewpatient Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "LastVerifiedDate": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/LastVerifiedDate",
                "type": "string",
                "title": "The Lastverifieddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PatientAgeLimitMin": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/PatientAgeLimitMin",
                "type": "string",
                "title": "The Patientagelimitmin Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "PatientAgeLimitMax": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/PatientAgeLimitMax",
                "type": "string",
                "title": "The Patientagelimitmax Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsVerified": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/IsVerified",
                "type": "string",
                "title": "The Isverified Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SubNetworkPracticeEffectiveDate": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/SubNetworkPracticeEffectiveDate",
                "type": "string",
                "title": "The Subnetworkpracticeeffectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SubNetworkPracticeTerminateDate": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/SubNetworkPracticeTerminateDate",
                "type": "string",
                "title": "The Subnetworkpracticeterminatedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsDelegated": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/IsDelegated",
                "type": "string",
                "title": "The Isdelegated Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DelegatedEffectiveDate": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/DelegatedEffectiveDate",
                "type": "string",
                "title": "The Delegatedeffectivedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DelegatedTerminationDate": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/DelegatedTerminationDate",
                "type": "string",
                "title": "The Delegatedterminationdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DelegatedTerminationReason": {
                "$id": "#/properties/Provider/properties/ProviderContractLine/items/properties/DelegatedTerminationReason",
                "type": "string",
                "title": "The Delegatedterminationreason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        },
        "ProviderStatus": {
          "$id": "#/properties/Provider/properties/ProviderStatus",
          "type": "array",
          "title": "The Providerstatus Schema",
          "items": {
            "$id": "#/properties/Provider/properties/ProviderStatus/items",
            "type": "object",
            "title": "The Items Schema",
            "required": [
              "NetworkName",
              "SubNetworkName",
              "TaxID",
              "Address1",
              "Address2",
              "City",
              "State",
              "Zip",
              "TaxonomyCode",
              "Status",
              "SubStatus",
              "StatusType",
              "SubmitDate",
              "AppReceivedDate",
              "CredStartDate",
              "CredEndDate",
              "DeclineDate",
              "CommGroup",
              "CommMeeting",
              "IsAppeal",
              "Reason",
              "Comments"
            ],
            "properties": {
              "NetworkName": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/NetworkName",
                "type": "string",
                "title": "The Networkname Schema",
                "default": "",
                "examples": [
                  "LTC Meridian"
                ],
                "pattern": "^(.*)$"
              },
              "SubNetworkName": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/SubNetworkName",
                "type": "string",
                "title": "The Subnetworkname Schema",
                "default": "",
                "examples": [
                  "Sub- LTC Meridian"
                ],
                "pattern": "^(.*)$"
              },
              "TaxID": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/TaxID",
                "type": "string",
                "title": "The Taxid Schema",
                "default": "",
                "examples": [
                  "814789658"
                ],
                "pattern": "^(.*)$"
              },
              "Address1": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/Address1",
                "type": "string",
                "title": "The Address1 Schema",
                "default": "",
                "examples": [
                  "92 W Lowder St Macclenny"
                ],
                "pattern": "^(.*)$"
              },
              "Address2": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/Address2",
                "type": "string",
                "title": "The Address2 Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "City": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/City",
                "type": "string",
                "title": "The City Schema",
                "default": "",
                "examples": [
                  "Jacksonville"
                ],
                "pattern": "^(.*)$"
              },
              "State": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/State",
                "type": "string",
                "title": "The State Schema",
                "default": "",
                "examples": [
                  "NC"
                ],
                "pattern": "^(.*)$"
              },
              "Zip": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/Zip",
                "type": "string",
                "title": "The Zip Schema",
                "default": "",
                "examples": [
                  "32063"
                ],
                "pattern": "^(.*)$"
              },
              "TaxonomyCode": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/TaxonomyCode",
                "type": "string",
                "title": "The Taxonomycode Schema",
                "default": "",
                "examples": [
                  "1223D0004X"
                ],
                "pattern": "^(.*)$"
              },
              "Status": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/Status",
                "type": "string",
                "title": "The Status Schema",
                "default": "",
                "examples": [
                  "Recruitment in Progress"
                ],
                "pattern": "^(.*)$"
              },
              "SubStatus": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/SubStatus",
                "type": "string",
                "title": "The Substatus Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "StatusType": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/StatusType",
                "type": "string",
                "title": "The Statustype Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "SubmitDate": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/SubmitDate",
                "type": "string",
                "title": "The Submitdate Schema",
                "default": "",
                "examples": [
                  "01/12/2020"
                ],
                "pattern": "^(.*)$"
              },
              "AppReceivedDate": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/AppReceivedDate",
                "type": "string",
                "title": "The Appreceiveddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CredStartDate": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/CredStartDate",
                "type": "string",
                "title": "The Credstartdate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CredEndDate": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/CredEndDate",
                "type": "string",
                "title": "The Credenddate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "DeclineDate": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/DeclineDate",
                "type": "string",
                "title": "The Declinedate Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CommGroup": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/CommGroup",
                "type": "string",
                "title": "The Commgroup Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "CommMeeting": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/CommMeeting",
                "type": "string",
                "title": "The Commmeeting Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "IsAppeal": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/IsAppeal",
                "type": "string",
                "title": "The Isappeal Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Reason": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/Reason",
                "type": "string",
                "title": "The Reason Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "Comments": {
                "$id": "#/properties/Provider/properties/ProviderStatus/items/properties/Comments",
                "type": "string",
                "title": "The Comments Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          }
        }
      }
    }
  }
}