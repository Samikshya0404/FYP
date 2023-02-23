import { AbstractControl, FormGroup } from '@angular/forms';




export function CheckPasswordMatch(password1: string, password2: string){
  return (formGroup: FormGroup) => {
    const passwordValue = formGroup.controls[password1];
    const conformPasswordValue = formGroup.controls[password2];
    if (conformPasswordValue.errors && !conformPasswordValue.errors.passwordMatch) {
        return;
    }
    if (passwordValue.value !== conformPasswordValue.value) {
        conformPasswordValue.setErrors({ passwordMatch: true });
    } else {
        conformPasswordValue.setErrors(null);
    }
}
}
