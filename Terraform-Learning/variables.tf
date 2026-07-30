#this files shows the variables used in the terraform script
variable "resource_group_name" {
    description = "Name of the resource group"
    type = string
}
variable "location" {
    description = "Azure Region"
    type = string
}