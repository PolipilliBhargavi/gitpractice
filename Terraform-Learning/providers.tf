# this files contains the providers required 
terraform {
    required_version = ">=1.15.0"
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = ">=3.0.0"
        }
    }
}
provider azurerm {
    features{}
}